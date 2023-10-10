import sqlite3


# create fuction config init db and config db in sqlite3
def config_db():
    # # create if not exists the database
    # with open("Sensores.db", "w") as file:
    #     pass
    # create connection to the database
    conn = sqlite3.connect("Sensores.db")
    # create cursor to the database
    cursor = conn.cursor()
    # create table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SensorPir (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensorPIR TEXT,
        fecha TEXT
        )"""
    )
    conn.commit()
    # create table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SensorDistance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensorDistance TEXT,
        fecha TEXT
        )"""
    )
    conn.commit()
    # create table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SensorTemperature (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensorTemperature TEXT,
        fecha TEXT
        )"""
    )
    conn.commit()
    # crete table humedad
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SensorHumedad (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensorHumedad TEXT,
        fecha TEXT
        )"""
    )
    conn.commit()
    # close the connection to the database
    conn.close()


# create function to get data from the database
def get_data_table(nameTable):
    # create connection to the database
    conn = sqlite3.connect("Sensores.db")
    # create cursor to the database
    cursor = conn.cursor()
    # get data from the database
    cursor.execute("SELECT * FROM " + nameTable)
    # save the data in a variable
    data = cursor.fetchall()
    print("data", data)
    # close the connection to the database
    conn.close()
    # return the data
    return data


# create function to save data in the database
def save_data(data):
    # create connection to the database
    conn = sqlite3.connect("Sensores.db")
    # create cursor to the database
    cursor = conn.cursor()
    # save data in the database
    if "sensorPIR" in data:
        cursor.execute(
            "INSERT INTO SensorPir (sensorPIR, fecha) VALUES (?, datetime('now', 'localtime'))",
            (data["sensorPIR"],),
        )
        conn.commit()
    if "sensorDistance" in data:
        cursor.execute(
            "INSERT INTO SensorDistance (sensorDistance, fecha) VALUES (?, datetime('now', 'localtime'))",
            (data["sensorDistance"],),
        )
        conn.commit()
    if "sensorTemperature" in data:
        cursor.execute(
            "INSERT INTO SensorTemperature (sensorTemperature, fecha) VALUES (?, datetime('now', 'localtime'))",
            (data["sensorTemperature"],),
        )
        conn.commit()
    if "sensorHumedad" in data:
        cursor.execute(
            "INSERT INTO SensorHumedad (sensorHumedad, fecha) VALUES (?, datetime('now', 'localtime'))",
            (data["sensorHumedad"],),
        )
        conn.commit()
    # close the connection to the database
    conn.close()


# create function to delete data from the database
def delete_data(id):
    # create connection to the database
    conn = sqlite3.connect("Sensores.db")
    # create cursor to the database
    cursor = conn.cursor()
    # delete data from the database
    cursor.execute("DELETE FROM Sensores WHERE id=?", (id,))
    # save the changes in the database
    conn.commit()
    # close the connection to the database
    conn.close()


# create function to update data from the database
def update_data(id, data):
    # create connection to the database
    conn = sqlite3.connect("Sensores.db")
    # create cursor to the database
    cursor = conn.cursor()
    # update data from the database
    cursor.execute(
        "UPDATE Sensores SET sensorPIR=?, sensorDistance=? WHERE id=?",
        (data["sensorPIR"], data["sensorDistance"], id),
    )
    # save the changes in the database
    conn.commit()
    # close the connection to the database
    conn.close()
