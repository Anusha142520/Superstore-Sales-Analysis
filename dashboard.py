import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Superstore.csv', encoding='latin1')

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Superstore Sales Analysis - Anusha', fontsize=16, fontweight='bold')

df.groupby('Category')['Sales'].sum().plot(kind='bar', ax=axes[0,0])
axes[0,0].set_title('Sales by Category')

df.groupby('Region')['Profit'].sum().plot(kind='bar', ax=axes[0,1], color='orange')
axes[0,1].set_title('Profit by Region')

df.groupby('Segment')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%', ax=axes[0,2])
axes[0,2].set_title('Sales by Segment')
axes[0,2].set_ylabel('')

df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().plot(ax=axes[1,0])
axes[1,0].set_title('Monthly Sales Trend')

df.groupby('Sub-Category')['Sales'].sum().sort_values().tail(5).plot(kind='barh', ax=axes[1,1], color='teal')
axes[1,1].set_title('Top 5 Sub-Category')

axes[1,2].scatter(df['Discount'], df['Profit'], alpha=0.3)
axes[1,2].set_title('Discount vs Profit')

plt.tight_layout(rect=[0,0,1,0.95])
plt.show()