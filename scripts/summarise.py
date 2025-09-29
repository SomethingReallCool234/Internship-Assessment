import pandas as pd
import os

# Load summary CSV files
stock = pd.read_csv('outputs/data_parsing/stock_summary.csv')
ad = pd.read_csv('outputs/data_parsing/ad_summary.csv')

# Rename column for consistency
stock = stock.rename(columns={'sku': 'identifier'})

# Merge summaries by product identifier
summary = pd.merge(stock, ad, on='identifier', how='outer')

# Compute KPIs safely handling zeros
summary['return_rate'] = summary['units_returned'] / summary['units_shipped'].replace(0, 1)
summary['ad_to_revenue_ratio'] = summary['ad_spend'] / summary['revenue'].replace(0, 1)
summary['velocity_per_unit'] = summary['velocity_score'] / summary['current_fba_inventory'].replace(0, 1)

# Calculate adaptive thresholds using quantiles
return_threshold = summary['return_rate'].quantile(0.9)
roi_threshold = summary['ad_to_revenue_ratio'].quantile(0.9)
velocity_threshold = summary['velocity_per_unit'].quantile(0.1)

# Apply flags based on adaptive thresholds
summary['high_return'] = summary['return_rate'] > return_threshold
summary['low_roi'] = summary['ad_to_revenue_ratio'] > roi_threshold
summary['low_velocity'] = summary['velocity_per_unit'] < velocity_threshold

# Print thresholds for awareness
print(f'Adaptive return rate threshold (90th percentile): {return_threshold}')
print(f'Adaptive ad to revenue ROI threshold (90th percentile): {roi_threshold}')
print(f'Adaptive velocity per unit threshold (10th percentile): {velocity_threshold}')

# Extract flagged products
flagged_high_return = summary[summary['high_return']]
flagged_low_roi = summary[summary['low_roi']]
flagged_low_velocity = summary[summary['low_velocity']]

# Save full diagnostics with flags
os.makedirs('outputs', exist_ok=True)
summary.to_csv('outputs/summary/product_kpi_diagnostics.csv', index=False)

# Save flagged groups separately for detailed review
flagged_high_return.to_csv('outputs/summary/high_return_products.csv', index=False)
flagged_low_roi.to_csv('outputs/summary/low_roi_products.csv', index=False)
flagged_low_velocity.to_csv('outputs/summary/low_velocity_products.csv', index=False)

print('\nDiagnostics and flagged product lists saved to outputs folder.')
