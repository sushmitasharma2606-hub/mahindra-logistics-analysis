import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
# Ensure 'mahindra_logistics_dataset.csv' is in the same folder as this script
df = pd.read_csv('mahindra_logistics_dataset.csv')

# 2. Feature Engineering
# Calculate key performance indicators (KPIs)
df['Cost_per_Volume'] = df['Cost'] / df['Shipment_Volume']
df['Profit'] = df['Revenue'] - df['Cost']
df['Profit_Margin_Pct'] = (df['Profit'] / df['Revenue']) * 100

# 3. Regional Efficiency Analysis
# Grouping by region to find where the "Last Mile" is most expensive/slow
region_stats = df.groupby('Region').agg({
    'Delivery_Time_Days': 'mean',
    'Cost_per_Volume': 'mean',
    'Shipment_Volume': 'sum',
    'Profit_Margin_Pct': 'mean'
}).sort_values('Delivery_Time_Days', ascending=False)

print("--- Regional Performance Summary ---")
print(region_stats)

# 4. Identifying Hub-Spoke & Micro-Warehousing Opportunities
# We look for high-cost, high-time, or specific industry clusters
bottlenecks = df.groupby(['Region', 'Industry']).agg({
    'Delivery_Time_Days': 'mean',
    'Cost_per_Volume': 'mean',
    'Shipment_Volume': 'sum'
}).reset_index().sort_values('Cost_per_Volume', ascending=False)

# 5. Visualizations
plt.style.use('ggplot')

# Chart A: Delivery Times by Region and Mode
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Region', y='Delivery_Time_Days', hue='Mode', palette='magma')
plt.title('Inefficiency Check: Delivery Time by Region & Transport Mode')
plt.axhline(df['Delivery_Time_Days'].mean(), color='red', linestyle='--', label='National Avg')
plt.legend()
plt.savefig('delivery_inefficiency.png')

# Chart B: Cost vs Volume (The Business Case for Micro-warehousing)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Shipment_Volume', y='Cost', hue='Region', size='Delivery_Time_Days', alpha=0.7)
plt.title('Cost vs Volume Distribution (Bubble Size = Delivery Time)')
plt.savefig('cost_volume_analysis.png')

# 6. Exporting Results for Report
region_stats.to_csv('regional_analysis_output.csv')
bottlenecks.to_csv('industry_bottlenecks.csv')

print("\nAnalysis Complete! Charts and CSV summaries have been generated.")
