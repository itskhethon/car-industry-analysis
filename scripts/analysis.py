import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Make sure the images/ folder exists
os.makedirs("images", exist_ok=True)

# Load the dataset
data = pd.read_csv("data/cars2.csv")

# Total car productions by country
def count_by_country(country):
    count = data[data['Country of Origin'] == country].shape[0]
    print(f"There are {count} car productions from {country}.")
    return count

# Example usage
count_by_country("Japan")

# Count cars with MPG 11.0 and 14.0
for mpg_value in [11.0, 14.0]:
    count = data[data['MPG'] == mpg_value].shape[0]
    print(f"There are {count} cars with MPG = {mpg_value}.")

# Cars with weight < 3000kg
light_cars = data[data['Weight/kg'] < 3000.0]
print(f"There are {len(light_cars)} cars with weight < 3000kg.")

# Cars with horsepower > 230
high_hp = data[data['No. of Horsepower'] > 230]
print(f"Number of cars with horsepower > 230: {len(high_hp)}")
print("Countries of origin:", high_hp['Country of Origin'].unique())
print("Car names:\n", high_hp['Name of the Car'].values)

# Cars with 4 or 8 cylinders
cyl_count = data[data['No. of Cylinders'].isin([4, 8])].shape[0]
print(f"There are {cyl_count} cars with 4 or 8 cylinders.")

# Save car names by country
def save_cars_by_country(country):
    car_list = data[data['Country of Origin'] == country]['Name of the Car']
    with open("Car-OriginCountry.txt", "w") as f:
        f.write("\n".join(car_list))
    print(f"Saved car names from {country} to Car-OriginCountry.txt.")

# Example usage
save_cars_by_country("US")

# Pie chart of car production by country
country_counts = data['Country of Origin'].value_counts()
country_counts.plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    title="Car Production by Country"
)
plt.axis("equal")
plt.savefig("images/pie_chart.png")
plt.clf()

# Section B: Stats
print("\n--- STATISTICS ---")
print("Max MPG:", data["MPG"].max())
print("Min MPG:", data["MPG"].min())
print("Max Cylinders:", data["No. of Cylinders"].max())
print("Min Cylinders:", data["No. of Cylinders"].min())
print("Max Weight:", data["Weight/kg"].max())
print("Min Weight:", data["Weight/kg"].min())

print("Heaviest car:", data.loc[data["Weight/kg"].idxmax(), "Name of the Car"])
print("Lightest car:", data.loc[data["Weight/kg"].idxmin(), "Name of the Car"])
print("Fastest acceleration:", data.loc[data["Acceleration/sec"].idxmax(), "Name of the Car"])
print("Slowest acceleration:", data.loc[data["Acceleration/sec"].idxmin(), "Name of the Car"])
print("Most horsepower:", data.loc[data["No. of Horsepower"].idxmax(), "Name of the Car"])
print("Least horsepower:", data.loc[data["No. of Horsepower"].idxmin(), "Name of the Car"])

# Histogram: Weight
data["Weight/kg"].plot(kind='hist', bins=[0, 2000, 4000, 6000], rwidth=0.8, color='green')
plt.title("Car Weights Distribution")
plt.xlabel("Weight (kg)")
plt.ylabel("Frequency")
plt.savefig("images/hist_weight.png")
plt.clf()

# Histogram: No. of Cylinders
data["No. of Cylinders"].plot(kind='hist', bins=[0, 4, 8, 12], rwidth=0.8, color='orange')
plt.title("Number of Cylinders Distribution")
plt.xlabel("No. of Cylinders")
plt.ylabel("Frequency")
plt.savefig("images/hist_cylinders.png")
plt.clf()

print("\nAll tasks completed successfully.")
