# Automated Weather ETL Pipeline

An automated Python ETL (Extract, Transform, Load) pipeline that fetches daily weather data, cleans it, and stores it in a local sqlite database. 

# Project Overview
This project demonstrates core data engineering concepts by building an end-to-end pipeline. It runs automatically on a daily schedule using Windows Task Scheduler, simulating a real-world production environment.

# How It Works
1. **Extract:** Fetches raw JSON weather data from the OpenWeatherMap API.
2. **Transform:** Uses `pandas` to clean the data, convert temperatures from Kelvin to Celsius, and format Unix timestamps into readable dates.
3. **Load:** Appends the clean data into a local SQLite database (`weather_data.db`).
4. **Automate:** A batch file and Windows Task Scheduler run the pipeline daily and log the results.

# ️ Tech Stack
* **Language:** Python
* **Libraries:** `requests`, `pandas`, `sqlite3`
* **Automation:** Windows Task Scheduler, Batch scripting
* **Database:** SQLite

# How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/jasonwambua31-eng/weather-ETL-pipeline.git
