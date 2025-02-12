
import pandas as pd
import random
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


# Generate some "French vs. Dutch" stereotype data
data = [
    {"Nationality": "French", "Loves": "Baguette", "Hates": "Speaking English", "Drinks": "Wine"},
    {"Nationality": "Dutch", "Loves": "Bicycles", "Hates": "Paying for things", "Drinks": "Beer"},
    {"Nationality": "French", "Loves": "Strikes", "Hates": "Working Mondays", "Drinks": "Coffee"},
    {"Nationality": "Dutch", "Loves": "Cheese", "Hates": "Hills", "Drinks": "Milk"},
    {"Nationality": "French", "Loves": "Philosophy", "Hates": "Fast Food", "Drinks": "Pastis"},
    {"Nationality": "Dutch", "Loves": "Directness", "Hates": "Small talk", "Drinks": "Tea"},
]

# Convert to a DataFrame
df = pd.DataFrame(data)

# Introduce some "messy" data
df.loc[random.randint(0, len(df) - 1), "Hates"] = None  # Missing value
df.loc[random.randint(0, len(df) - 1), "Drinks"] = "CocaCola"  # "Wrong" data

# Clean the data: Fill missing values
df["Hates"].fillna("Nothing (Too chill to hate)", inplace=True)

# Normalize "Drinks" column: Replace unexpected drinks
df["Drinks"] = df["Drinks"].apply(lambda x: "Beer" if x == "CocaCola" else x)

# Analyze the most common traits
most_loved = df["Loves"].mode()[0]
most_hated = df["Hates"].mode()[0]
most_drunk = df["Drinks"].mode()[0]

# Print the funny analysis
print(f"""
French VS Dutch - A Completely Serious and Scientific Analysis 

Most Loved Thing Overall: {most_loved}
Most Hated Thing Overall: {most_hated}
Most Consumed Drink: {most_drunk}

Conclusion: The French are probably on strike while the Dutch cycle around them, avoiding hills and spending no money. 
Meanwhile, both nations continue their eternal struggle over who has the best cheese. 
""")
