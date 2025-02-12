import random

# Funny European-style weather phrases
weather_reports = [
    ("UK", "It's raining. Again. Might stop next year."),
    ("France", "Strike scheduled for tomorrow due to excessive sunshine."),
    ("Netherlands", "Strong winds expected. Hold onto your bicycles."),
    ("Germany", "Cloudy with a 99% chance of efficiency."),
    ("Italy", "Too hot for work, perfect for espresso."),
    ("Spain", "Siesta conditions perfect. Chance of work: 0%"),
    ("Sweden", "Winter is coming. No one is surprised."),
    ("Belgium", "Rainy, just like yesterday. And the day before."),
]

# Select a random forecast
country, forecast = random.choice(weather_reports)

# Print the report
print(f"📍 {country}: {forecast}")
