# aqi-tracker
🌫️ Air Quality Index (AQI) Data Collector using OpenWeather API and SQLite
A beginner-friendly Python project to fetch real-time AQI data, store it in a local SQLite database, and avoid duplicate entries based on latitude and longitude.

Features
• Fetches AQI and pollutant component data from the OpenWeather API
• Dynamically stores data in a local SQLite database
• Avoids duplicate entries based on latitude and longitude
• Displays all historical AQI records in the terminal
• Supports full table reset using a drop function

How It Works

    Accepts user input for latitude, longitude, and OpenWeather API key

    Sends a request to the OpenWeather Air Pollution API

    Parses the AQI and maps it to a readable format (Good, Moderate, etc.)

    Converts Unix timestamp to human-readable date and time

    Inserts data into SQLite only if not already present

    Displays all stored AQI records

    Offers an option to drop (reset) the database table

Technologies Used
• Python 3
• SQLite3
• Requests
• OpenWeather API

File Structure
fetch_aqi.py → Main logic for API interaction and database handling
db_manager.py → Helper functions: connect, insert, fetch, drop
aqi_data.db → SQLite database (created automatically)

Sample Output

Enter the Latitude and the Longitude: 28.6139 77.2090  
Enter the API Key to fetch: your_api_key_here  

The data is fetched successfully!  
The Air Quality Index is: 3  
The Components attributed for Air Pollution are: {'co': ..., 'pm2_5': ..., ...}  
The Air Quality is: Moderate  
Timestamp: 2025-08-01 01:22:40  

DB Created!  
New Record Inserted Successfully!  

ID: 1 || AQI: 3 || LAT: 28.6139 || LON: 77.209 || timestamp: 2025-08-01 01:22:40  

Notes
• Get a free API key at https://openweathermap.org/api
• Prevents duplicates based on lat and lon only (timestamp not used for uniqueness)
• Use the drop() function to clear the database table

Let me know if you’d like:
• A requirements.txt
• A GitHub logo badge
• A demo GIF or screenshot
• A deployment option (like a scheduled script)
