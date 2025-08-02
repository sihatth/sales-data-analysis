import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

# Load the CSV
df = pd.read_csv("sales_data.csv")

# Step 1: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 2: Preview the data
print("🧾 Column names:")
print(df.columns.tolist())
print("\n📄 First 5 rows:")
print(df.head())
print("\n📊 Data Summary:")
print(df.describe())

# Step 3: Ensure revenue column exists
if 'revenue' not in df.columns:
    df['revenue'] = df['order_quantity'] * df['unit_price']

# Step 4: Group revenue by country
revenue_by_country = df.groupby('country')['revenue'].sum()
print("\n💰 Total Revenue by Country:")
print(revenue_by_country)

# Step 5: Average units sold per product
avg_units = df.groupby('product')['order_quantity'].mean()
print("\n📦 Average Units Sold per Product:")
print(avg_units)

# Step 6: Bar chart - Revenue by Country
revenue_by_country.plot(kind='bar', title='Revenue by Country', xlabel='Country', ylabel='Revenue', color='skyblue')
plt.tight_layout()
plt.savefig("charts/revenue_by_country.png")
plt.show()

# Step 7: Pie chart - Top 10 Products by Units Sold
units_by_product = df.groupby('product')['order_quantity'].sum()
top_products = units_by_product.sort_values(ascending=False).head(10)

# Add "Other"
other = units_by_product.sum() - top_products.sum()
top_products['Other'] = other

top_products.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Units Sold by Top 10 Products')
plt.ylabel('')
plt.tight_layout()
plt.savefig("charts/units_sold_by_product.png")
plt.show()
