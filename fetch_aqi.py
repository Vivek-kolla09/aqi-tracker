import requests
from datetime import datetime
from db_manager import conn_db, createDB,insertDB,fetch,drop
def getinfo(lat,lon,api_key):    
    main_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response_request = requests.get(main_url)

    # print(response_request)
    if response_request.status_code == 200:
        print("The data is fetched successfully!")
        aqi_data = response_request.json()
        return aqi_data
    else:
        print("Failed to fetch/retrieve the data!")
        print("Please try again after sometime...")
        return None


lat,lon = map(float,input("Enter the Latitude and the Longitude: ").split())
api_key = input("Enter the API Key to fetch: ")
aqi_info = getinfo(lat,lon,api_key)

if aqi_info:
    # data = aqi_info['list'][0]['main']['aqi']
    print(f"The Air Quality Index is: {aqi_info['list'][0]['main']['aqi']}")
    print(f"The Components attributed for Air Pollution are: {aqi_info['list'][0]['components']}")
    # print(f"TimeStamp: {aqi_info['list'[0]['main']['dt']]}")

aqi = aqi_info['list'][0]['main']['aqi']
aqi_mapping = {
    1:'Good',
    2:'Fair',
    3:'Moderate',
    4:'Poor',
    5:'Very Poor'
}
mapped = aqi_mapping.get(aqi)
if mapped is not None:
    print(f"The Air Quality is: {mapped}")
else:
    print("Not found")
time_stamp = aqi_info['list'][0]['dt'] #Unix Time (Epoch Time) format
read_ts = datetime.fromtimestamp(time_stamp)
print(f"Timestamp: {read_ts}") #The UNIX Time Stamp is converted into the normal date and time stamp

def db_info():
    db_data  = {
        "aqi": aqi,
        "lat": lat,
        "lon": lon,
        "timestamp":read_ts
    }
    return db_data

# Saving to database
con,c = conn_db()
createDB(c)
insertDB(c,db_info())
fetch(c)
con.commit()
con.close()

