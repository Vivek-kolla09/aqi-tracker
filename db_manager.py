import sqlite3
def conn_db():
    con = sqlite3.connect('aqi_data.db')
    c = con.cursor()
    return con,c
def createDB(c):
    c.execute('''CREATE TABLE IF NOT EXISTS air_quality (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aqi INTEGER,
        lat REAL,
        lon REAL,
        timestamp TEXT
    );''')
    print("DB Created!")

def insertDB(c,data):
    c.execute(''' SELECT * FROM air_quality WHERE lat=? AND lon=?''', (data['lat'],data['lon']))
    res = c.fetchone()
    if res is None:
        c.execute('''INSERT INTO air_quality(aqi,lat,lon,timestamp) VALUES (?,?,?,?) ''',(data['aqi'],data['lat'],data['lon'],data['timestamp']))
        print("New Record Inserted Successfully!")
    else:
        print("Record already exists!")

def fetch(c):
    c.execute('''SELECT * FROM air_quality''')
    records = c.fetchall()
    for rec in records:
        print(f'''ID: {rec[0]} || AQI: {rec[1]} || LAT: {rec[2]} || LON: {rec[3]} || timestamp: {rec[4]}''')

def drop(c):
    c.execute("DROP TABLE IF EXISTS air_quality")
    print("All tables dropped.")
