import sqlite3
import datetime

# Connect to the database (creates a new file if it doesn't exist)

# Create a table named garbagedump with place and time columns
# conn.execute('''
#     CREATE TABLE IF NOT EXISTS garbagedump (
#         place TEXT,
#         timeOfReporting DateTime DEFAULT CURRENT_TIMESTAMP,
#         timeOfCleaning DateTime
#     )
# ''')

# Insert a record into the garbagedump table
# conn.execute("INSERT INTO garbagedump (place, time) VALUES ('Some place', '2022-01-01 10:00:00')")

def insertGarbageDump(place):
    # Get the current date and time
    conn = sqlite3.connect('garbage.db')
    current_datetime = datetime.datetime.now()

    # Add 3 days to the current date and time
    timeOfCleaning = current_datetime + datetime.timedelta(days=3)
    conn.execute("INSERT INTO garbagedump (place, timeOfCleaning) VALUES (?, ?)", (place, timeOfCleaning))

# Commit the changes
    conn.commit()

# Close the connection
    conn.close()