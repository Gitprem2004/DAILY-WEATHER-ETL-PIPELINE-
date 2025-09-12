# DAILY-WEATHER-ETL-PIPELINE-
A data engineering project demonstrating a daily automated ETL process. Extracts weather data via API, transforms with Python/PandAS, and stores it in a SQL database.

## 📜 Project Overview
This project is a complete, automated ETL (Extract, Transform, Load) pipeline built with Python. It fetches daily weather data for multiple cities from a live REST API, processes the raw data, and stores it in a PostgreSQL database. The entire process is scheduled to run daily without any manual intervention, creating a reliable and consistently updated historical weather dataset.

This project serves as a practical demonstration of fundamental data engineering principles, including data extraction from APIs, data transformation, database management, and workflow automation.

---

## 🎯 Project Goal
The primary objective is to build a robust, hands-free data pipeline that automatically collects and stores data, making it ready for future analysis, visualization in BI tools like Power BI, or machine learning applications.

---

## ⚙️ ETL Pipeline Architecture
The pipeline is structured in three main stages:

1.  **Extract:** A Python script calls the [WeatherAPI.com](http://WeatherAPI.com) REST API endpoint to fetch current weather data for a predefined list of cities. The raw data is received in JSON format.

2.  **Transform:** The raw JSON data is parsed and structured using the **Pandas** library. This stage involves:
    - Selecting only the relevant data fields (e.g., city, temperature, humidity).
    - Cleaning the data and ensuring correct data types.
    - Organizing the data into a clean DataFrame that matches the schema of the target database table.

3.  **Load:** The transformed data, now in a Pandas DataFrame, is loaded into a **PostgreSQL** database using the **SQLAlchemy** and **psycopg2** libraries. The script appends the new data, allowing for the collection of historical records over time.

---

## 🛠️ Tools & Technologies
- **Programming Language:** Python
- **Libraries:**
    - `requests`: For making HTTP requests to the API.
    - `pandas`: For data manipulation and transformation.
    - `SQLAlchemy` & `psycopg2`: For connecting to and loading data into the PostgreSQL database.
- **Database:** PostgreSQL
- **Automation:** Windows Task Scheduler

---

## 🚀 How to Run This Project
To replicate this project on your local machine, follow these steps:

1.  **Prerequisites:**
    - Python 3.x installed.
    - PostgreSQL server installed and running.

2.  **Installation:**
    - Clone this repository.
    - Install the required Python libraries:
      ```bash
      pip install requests pandas sqlalchemy psycopg2-binary
      ```

3.  **Database Setup:**
    - Create a database in PostgreSQL (e.g., `api_data`).
    - Run the following SQL command to create the target table:
      ```sql
      CREATE TABLE weather_data (
          city VARCHAR(50),
          temperature_celsius FLOAT,
          weather_condition VARCHAR(100),
          humidity INTEGER,
          record_time TIMESTAMP
      );
      ```

4.  **Configuration:**
    - Obtain a free API key from [WeatherAPI.com](https://www.weatherapi.com/).
    - Open the `etl.py` script and update the `api_key` and database connection string with your credentials.

5.  **Execution:**
    - Run the script from your terminal:
      ```bash
      python etl.py
      ```

---

## ⏰ Automation
The pipeline is scheduled for daily execution using **Windows Task Scheduler**, which runs a simple `.bat` script to trigger the Python ETL process automatically, ensuring the dataset is updated consistently.
