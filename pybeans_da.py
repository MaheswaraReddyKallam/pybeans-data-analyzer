import pandas as pd

# ==========================================
# 1. DATA INGESTION & EXPORT
# ==========================================
raw_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Item": ["Espresso", "Latte", "Latte", "Black Coffee", "Espresso", "Latte", "Black Coffee"],
    "Units_Sold": [45, 60, 0, 30, 55, 80, 0],
    "Price_Per_Unit": [3.00, 4.50, 4.50, 2.50, 3.00, 4.50, 2.50]
}

df = pd.DataFrame(raw_data)
df.to_csv("coffee.csv", index=False)

# ==========================================
# 2. DATA CLEANING & FEATURE ENGINEERING
# ==========================================
# Filter out closed-store days (zero units sold)
df = df[df["Units_Sold"] != 0] 

# Calculate revenue metrics
df["Total_Revenue"] = df["Units_Sold"] * df["Price_Per_Unit"]

# ==========================================
# 3. INTERACTIVE CLI APPLICATION
# ==========================================
while True:
    menu = """
--- PyBeans Coffee Analyzer --- 
1. Show all clean data 
2. Show total weekly revenue 
3. Show revenue by item 
4. Exit
"""
    print(menu)

    opt = int(input("Enter your Option: "))

    if opt == 1:
        print("\n--- Cleaned Data ---")
        print(df)
    elif opt == 2:
        print(f"\nTotal Revenue for the week: ${df['Total_Revenue'].sum():.2f}")
    elif opt == 3:
        print("\n--- Revenue By Item ---")
        print(df.groupby("Item")["Total_Revenue"].sum())
    elif opt == 4:
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice, try again.")
