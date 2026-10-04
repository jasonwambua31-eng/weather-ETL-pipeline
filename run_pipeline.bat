@echo off
:: This moves the terminal into your project folder
cd /d C:\users\user\jason\weather_etl_project

:: This runs your load.py file (which triggers extract and transform)
:: It also saves all the print statements into a file called pipeline_log.txt
python load.py >> pipeline_log.txt 2>&1