import pandas as pd

# 1. Load the Data
raw_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Item": ["Espresso", "Latte", "Latte", "Black Coffee", "Espresso", "Latte", "Black Coffee"],
    "Units_Sold": [45, 60, 0, 30, 55, 80, 0], # Notice the zeros!
    "Price_Per_Unit": [3.00, 4.50, 4.50, 2.50, 3.00, 4.50, 2.50]
}

df = pd.DataFrame(raw_data)
df.to_csv("coffee.csv",index = False)

# 2. Clean and Engineer the Data (Done BEFORE the loop!)
# faster and less typing to just keep what you want rather than drop what you don't want.
# Your loop should only be used for displaying data, not altering it.

df = df[df["Units_Sold"] != 0] 
df["Total_Revenue"] = df["Units_Sold"] * df["Price_Per_Unit"]

# 3. The Interactive Application
while(True):
    menu = """--- PyBeans Coffee Analyzer --- 
        1. Show all clean data 
        2. Show total weekly rvenue 
        3. Show revenue by item 
        4. Exit """
    print(menu)

    opt = int(input("Enter your Option: "))

    if (opt == 1):
        print(df)
    elif (opt == 2):
        print("Total Revenue for the week: ", df["Total_Revenue"].sum())
    elif (opt == 3):
        print(df.groupby("Item")["Total_Revenue"].sum())
    elif (opt == 4):
        print("Good bye!")
        break
    else:
        print("Invalid choice, try again")

