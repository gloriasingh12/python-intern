import requests
import matplotlib.pyplot as plt

# 1. API Setup
API_KEY = "895284a22d0353443572d4d71520623e" # Use your OpenWeatherMap key
CITIES = ["Noida", "Delhi", "Mumbai", "Bangalore", "Chennai"]
temp_list = []

print("--- Fetching Real-time Weather Data ---")

# 2. Data Fetching Logic
for city in CITIES:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("main"):
        temp = response["main"]["temp"]
        temp_list.append(temp)
        print(f"{city}: {temp}°C")
    else:
        print(f"Error fetching data for {city}")

# 3. Data Visualization Dashboard
plt.figure(figsize=(10, 6))
colors = ['skyblue', 'orange', 'lightgreen', 'pink', 'gold']

# Creating the Bar Chart
bars = plt.bar(CITIES, temp_list, color=colors, edgecolor='black')

# Adding Data Labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}°C', ha='center', va='bottom', fontweight='bold')

# Styling the Dashboard
plt.title('Live Temperature Comparison Across Cities', fontsize=16, fontweight='bold')
plt.xlabel('City Name', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Displaying the Dashboard
plt.show()
