
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

# Pick a random nationality to analyze
random_nationality = random.choice(["French", "Dutch"])
filtered_df = df[df["Nationality"] == random_nationality]

# Randomly select one value from each category
most_loved = random.choice(filtered_df["Loves"].tolist())
most_hated = random.choice(filtered_df["Hates"].tolist())
most_drunk = random.choice(filtered_df["Drinks"].tolist())

# Print the funny analysis
print(f"""
French VS Dutch - A Completely Serious and Scientific Analysis 

Analyzing the {random_nationality} people...

Most Loved Thing: {most_loved}
Most Hated Thing: {most_hated}
Most Consumed Drink: {most_drunk}

Conclusion: The {random_nationality} are continuing their traditions. The French might be on strike, while the Dutch are cycling past them, avoiding hills and spending no money. 
Meanwhile, both nations still can't agree on whose cheese is better. 
""")
