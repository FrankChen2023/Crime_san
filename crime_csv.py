import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('crime_data.db')
cur = conn.cursor()

# drop and create the new tables
conn.execute('DROP TABLE IF EXISTS crime_date')
conn.execute('DROP TABLE IF EXISTS crime_position')
print("table dropped successfully")

# create the tables again
conn.execute('CREATE TABLE crime_date (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, week TEXT, district TEXT, address TEXT)')
conn.execute('CREATE TABLE crime_position (id INTEGER PRIMARY KEY AUTOINCREMENT, district TEXT, address TEXT, longitude FLOAT, latitude FLOAT)')

with open('DataSource_crime/crime.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        date = row[0]
        week = row[1]
        district = row[2]
        address = row[3]
        longitude = float(row[4])
        latitude = float(row[5])
        
        cur.execute('INSERT INTO crime_date VALUES (NULL,?,?,?,?)', (date, week, district, address))
        cur.execute('INSERT INTO crime_position VALUES (NULL,?,?,?,?)', (district, address, longitude, latitude))
        conn.commit()
print("data parsed successfully!")
conn.close()
