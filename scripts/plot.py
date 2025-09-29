import os
import pandas as pd
import matplotlib.pyplot as plt

# Load data
summary = pd.read_csv('outputs/summary/product_kpi_diagnostics.csv')

# Thresholds
return_threshold = summary['return_rate'].quantile(0.9)
roi_threshold = summary['ad_to_revenue_ratio'].quantile(0.9)
velocity_threshold = summary['velocity_per_unit'].quantile(0.1)

# Ensure directories exist
os.makedirs('outputs/plots', exist_ok=True)

def label_points(ax, df, x_col, y_col, label_col):
    for _, row in df.iterrows():
        ax.text(row[x_col], row[y_col], str(row[label_col]), fontsize=8, alpha=0.7)

# Plot 1: Return Rate vs Velocity Score
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(summary['return_rate'], summary['velocity_score'], color='gray', alpha=0.5, label='Normal')
ax.scatter(summary[summary['high_return']]['return_rate'], summary[summary['high_return']]['velocity_score'],
           color='red', s=100, label='High Return')
ax.scatter(summary[summary['low_roi']]['return_rate'], summary[summary['low_roi']]['velocity_score'],
           color='orange', s=100, label='Low ROI')
ax.scatter(summary[summary['low_velocity']]['return_rate'], summary[summary['low_velocity']]['velocity_score'],
           color='blue', s=100, label='Low Velocity')

ax.axvline(return_threshold, color='red', linestyle='--', label=f'Return Threshold ({return_threshold:.2f})')
ax.axhline(velocity_threshold, color='blue', linestyle='--', label=f'Velocity Threshold ({velocity_threshold:.2f})')

label_points(ax, summary[summary['high_return']], 'return_rate', 'velocity_score', 'identifier')
label_points(ax, summary[summary['low_roi']], 'return_rate', 'velocity_score', 'identifier')
label_points(ax, summary[summary['low_velocity']], 'return_rate', 'velocity_score', 'identifier')

ax.set_xlabel('Return Rate')
ax.set_ylabel('Velocity Score')
ax.set_title('Return Rate vs Velocity Score with Flags and Labels')
ax.legend()
plt.tight_layout()

# Save plot to both folders
plt.savefig('outputs/plots/return_vs_velocity_labels.png')
plt.close()

# Plot 2: Ad to Revenue Ratio vs Velocity Score
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(summary['ad_to_revenue_ratio'], summary['velocity_score'], color='gray', alpha=0.5, label='Normal')
ax.scatter(summary[summary['high_return']]['ad_to_revenue_ratio'], summary[summary['high_return']]['velocity_score'],
           color='red', s=100, label='High Return')
ax.scatter(summary[summary['low_roi']]['ad_to_revenue_ratio'], summary[summary['low_roi']]['velocity_score'],
           color='orange', s=100, label='Low ROI')
ax.scatter(summary[summary['low_velocity']]['ad_to_revenue_ratio'], summary[summary['low_velocity']]['velocity_score'],
           color='blue', s=100, label='Low Velocity')

ax.axvline(roi_threshold, color='orange', linestyle='--', label=f'ROI Threshold ({roi_threshold:.2f})')
ax.axhline(velocity_threshold, color='blue', linestyle='--', label=f'Velocity Threshold ({velocity_threshold:.2f})')

label_points(ax, summary[summary['high_return']], 'ad_to_revenue_ratio', 'velocity_score', 'identifier')
label_points(ax, summary[summary['low_roi']], 'ad_to_revenue_ratio', 'velocity_score', 'identifier')
label_points(ax, summary[summary['low_velocity']], 'ad_to_revenue_ratio', 'velocity_score', 'identifier')

ax.set_xlabel('Ad to Revenue Ratio')
ax.set_ylabel('Velocity Score')
ax.set_title('Ad to Revenue Ratio vs Velocity Score with Flags and Labels')
ax.legend()
plt.tight_layout()

# Save plot to both folders
plt.savefig('outputs/plots/ad_to_revenue_vs_velocity_labels.png')
plt.close()
