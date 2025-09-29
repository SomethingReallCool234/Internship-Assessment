import pandas as pd
import json
import os

# Create outputs folder if it doesn't exist
os.makedirs('outputs', exist_ok = True)

# Load CSV files
catalog_df = pd.read_csv('scripts/given_dataset/internal_catalog_dump.csv') 
inventory_df = pd.read_csv('scripts/given_dataset/inventory_movements.csv')
performance_df = pd.read_csv('scripts/given_dataset/performance_metrics.csv')

# Load JSON files
with open('scripts/given_dataset/marketplace_snapshot.json') as f:
    marketplace_snapshot = json.load(f)

with open('scripts/given_dataset/competitor_intelligence.json') as f:
    competitor_intelligence = json.load(f)

# Convert date columns to datetime
inventory_df['date'] = pd.to_datetime(inventory_df['date'], errors='coerce')
performance_df['week_ending'] = pd.to_datetime(performance_df['week_ending'], errors='coerce')
catalog_df['launch_date'] = pd.to_datetime(catalog_df['launch_date'], errors='coerce')

# Fill missing numeric values where appropriate
inventory_df.fillna({'units_shipped':0, 'units_returned':0, 'current_fba_inventory':0, 'velocity_score':0}, inplace=True)
performance_df.fillna({'search_rank_avg':-1}, inplace=True)

# Merge catalog and inventory on SKU/item_code
merged_df = pd.merge(inventory_df, catalog_df, left_on='sku', right_on='item_code', how='left')

# Summarize key metrics
stock_summary = merged_df.groupby('sku')[['units_shipped', 'units_returned', 'current_fba_inventory', 'velocity_score']].sum()
ad_summary = performance_df.groupby(['identifier'])[['ad_spend', 'revenue']].sum()

# Print summaries for initial review
stock_summary.to_csv('outputs/data_parsing/stock_summary.csv') 
ad_summary.to_csv('outputs/data_parsing/ad_summary.csv')

print("Summaries saved to outputs folder.")
