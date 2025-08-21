import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create output folder if it doesn't exist
os.makedirs('output', exist_ok=True)

# Sample data generation (simulates supply chain metrics; replace with pd.read_csv('your_data.csv') for real data)
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'] * 20,  # 100 rows
    'Sales': np.random.randint(100, 2000, 100),
    'Inventory': np.random.randint(50, 1000, 100),
    'Lead_Time': np.random.randint(5, 45, 100),
    'Order_Quantity': np.random.randint(50, 300, 100),
    'Shipping_Cost': np.random.uniform(5, 100, 100),
}
df = pd.DataFrame(data)

# Data processing and analysis (automated pipeline)
df['Inventory_Turnover'] = df['Sales'] / df['Inventory']  # KPI: Measures efficiency
df['Total_Cost'] = df['Shipping_Cost'] * df['Order_Quantity']  # KPI: Total shipping costs

# Build and manage KPIs
kpis = df.groupby('Product').agg({
    'Inventory_Turnover': 'mean',
    'Total_Cost': 'sum',
    'Lead_Time': 'mean'
}).reset_index()

# Print KPIs for reporting
print("Key Performance Indicators (KPIs):")
print(kpis)

# Data visualization (intuitive dashboards)
# Bar chart for average inventory turnover
kpis.plot(x='Product', y='Inventory_Turnover', kind='bar', legend=False)
plt.title('Average Inventory Turnover by Product')
plt.ylabel('Turnover Ratio')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('output/inventory_turnover.png')
plt.close()

# Scatter plot for lead time vs shipping cost (identify process issues)
df.plot.scatter(x='Lead_Time', y='Shipping_Cost', c='Inventory_Turnover', colormap='viridis')
plt.title('Lead Time vs Shipping Cost (Colored by Turnover)')
plt.savefig('output/lead_vs_cost.png')
plt.close()

# Additional insights: Query-like filtering (simulates SQL queries)
high_turnover_products = df[df['Inventory_Turnover'] > 1.5]['Product'].unique()
print(f"\nProducts with high inventory turnover (>1.5): {high_turnover_products}")

print("\nAnalysis complete. Visualizations saved in 'output/' folder.")
