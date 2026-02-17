import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. CREATE SAMPLE RETAIL DATA
# -------------------------------
data = {
    "Date": [
        "2025-01-01","2025-01-01","2025-01-02","2025-01-02",
        "2025-01-03","2025-01-03","2025-01-04","2025-01-04",
        "2025-01-05","2025-01-05","2025-01-06","2025-01-06",
        "2025-01-07","2025-01-07"
    ],
    "Product": [
        "Laptop","Mouse","Laptop","Keyboard",
        "Mouse","Monitor","Laptop","Monitor",
        "Keyboard","Mouse","Laptop","Keyboard",
        "Monitor","Mouse"
    ],
    "Sales": [
        1200,25,1150,45,
        30,300,1300,280,
        50,35,1250,60,
        310,40
    ]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

print("\n=== DATA SAMPLE ===")
print(df)

# -------------------------------
# 2. DAILY SALES TREND
# -------------------------------
daily_sales = df.groupby("Date")["Sales"].sum()

plt.figure()
daily_sales.plot(marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_sales_trend.png")
plt.show()

# -------------------------------
# 3. TOTAL SALES BY PRODUCT
# -------------------------------
product_sales = df.groupby("Product")["Sales"].sum()

plt.figure()
product_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# -------------------------------
# 4. SALES SHARE (PIE CHART)
# -------------------------------
plt.figure()
product_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Contribution by Product")
plt.ylabel("")
plt.tight_layout()
plt.savefig("sales_share.png")
plt.show()

# -------------------------------
# 5. WEEKDAY DEMAND PATTERN
# -------------------------------
df["Day"] = df["Date"].dt.day_name()
day_sales = df.groupby("Day")["Sales"].sum()

# order days correctly
order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day_sales = day_sales.reindex(order)

plt.figure()
day_sales.plot(kind='bar')
plt.title("Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weekday_sales.png")
plt.show()

# -------------------------------
# 6. KEY BUSINESS INSIGHTS
# -------------------------------
print("\n===== BUSINESS INSIGHTS =====")

print("Peak sales day:", daily_sales.idxmax().date())
print("Lowest sales day:", daily_sales.idxmin().date())
print("Top selling product:", product_sales.idxmax())

total_sales = product_sales.sum()
print("\nSales contribution (%)")
print((product_sales / total_sales * 100).round(2))
