import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import sqlite3

# =============================================================================
# --- 1. EXTRACT ---
# =============================================================================

# Replace with the API key you received from WeatherAPI.com
api_key = '32fa7f0529574cd6b17174931251109'
cities = ['Chennai', 'Bangalore', 'Mumbai', 'Delhi', 'Kolkata']
all_weather_data = []

print("Step 1: Starting data extraction...")
for city in cities:
    # This is the API endpoint we are calling
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    # Make the request to the API
    response = requests.get(url)
    
    # Check if the request was successful (a status code of 200 means "OK")
    if response.status_code == 200:
        data = response.json()
        all_weather_data.append(data)
        print(f"Successfully fetched data for {city}")
    else:
        print(f"Failed to get data for {city}. Status Code: {response.status_code}")

print("Extraction complete.\n")


# =============================================================================
# --- 2. TRANSFORM ---
# =============================================================================

print("Step 2: Starting data transformation...")
transformed_data = []
for data in all_weather_data:
    # We are picking only the fields that match our database table
    transformed_data.append({
        'city': data['location']['name'],
        'temperature_celsius': data['current']['temp_c'],
        'weather_condition': data['current']['condition']['text'],
        'humidity': data['current']['humidity'],
        'record_time': datetime.now()
    })

# Create a Pandas DataFrame for easier data manipulation
df = pd.DataFrame(transformed_data)

print("Transformation complete. Data preview:")
print(df.head())
print("\n")


# =============================================================================
# --- 3. LOAD ---
# =============================================================================

print("Step 3: Starting data load...")
try:
    # Create a connection engine to your PostgreSQL database.
    # Format: postgresql://[user]:[password]@[host]:[port]/[database]
    # **REPLACE 'your_password' with your actual PostgreSQL password**
    engine = create_engine('postgresql://postgres:Pdxxxx@localhost:5432/api_data')
    
    # Load the DataFrame into the 'weather_data' table.
    # 'if_exists='append'' means we will add new rows, not overwrite the table.
    df.to_sql('weather_data', engine, if_exists='append', index=False)
    
    print("Data loaded successfully into the 'weather_data' table!")
except Exception as e:

    print(f"Data load failed: {e}")
