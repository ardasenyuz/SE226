import mysql.connector

dataBase = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(dataBase)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE MyNewDatabase")

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database='MyNewDatabase',
  password=""
)

if connection.is_connected():
  db_info = connection.get_server_info()
  print("Connected to MySQL Server version ", db_info)
  cursor = connection.cursor()
  cursor.execute("select database();")
  record = cursor.fetchone()
  print("You are connected to database: ", record)


mySql_Create_Table_Query = """CREATE TABLE Marvel (
Id int(23) NOT NULL,
Movie varchar(50) NOT NULL,
Date varchar(50) NOT NULL,
MCU_Phase varchar(50) NOT NULL,
PRIMARY KEY (Id))"""

cursor = connection.cursor()
result = cursor.execute(mySql_Create_Table_Query)
print("Marvel table created successfully ")

mySql_insert_query = """INSERT INTO Students (Id, Movie, Date, MCU_Phase)
VALUES (%s, %s, %s, %s) """

records_to_insert = [(1, 'IronMan', 'May2,2008', 'Phase1'),
                     (2, 'TheIncredibleHulk',	'June13,2008', 'Phase1'),
                     (3, 'IronMan2', 'May7,2010', 'Phase1'),
                     (4, 'Thor', 'May7,2010', 'Phase1'),
                     (5, 'CaptainAmerica:TheFirstAvenger', 'July22,2011', 'Phase1'),
                     (6, "Marvel'sTheAvengers",	'May4,2012', 'Phase1'),
                     (7, 'IronMan3', 'May3,2013', 'Phase2'),
                     (8, 'Thor:TheDarkWorld', 'November8,2013',	'Phase2'),
                     (9, 'CaptainAmerica:TheWinterSoldier',	'April4,2014', 'Phase2'),
                     (10, 'GuardiansoftheGalaxy', 'August1,2014', 'Phase2'),
                     (11, 'Avengers:AgeofUltron', 'May1,2015', 'Phase2'),
                     (12, 'Ant-Man', 'July17,2015', 'Phase2'),
                     (13, 'CaptainAmerica:CivilWar', 'May6,2016', 'Phase3'),
                     (14, 'DoctorStrange', 'November4,2016', 'Phase3'),
                     (15, 'GuardiansoftheGalaxyVol.2', 'May5,2017', 'Phase3'),
                     (16, 'Spider-Man:Homecoming', 'July7,2017', 'Phase3'),
                     (17, 'Thor:Ragnarok', 'November3,2019', 'Phase3'),
                     (18, 'BlackPanther', 'February16,2018', 'Phase3'),
                     (19, 'Avengers:Infinity War', 'April27,2018', 'Phase3'),
                     (20, 'Ant-ManandtheWasp', 'July6,2018', 'Phase3'),
                     (21, 'CaptainMarvel', 'March8,2019', 'Phase3'),
                     (22, 'Avengers:Endgame', 'April26,2019', 'Phase3'),
                     (23, 'Spider-Man:FarFromHome',	'July2,2019', 'Phase3'),]

cursor=connection.cursor()
cursor.executemany(mySql_insert_query, records_to_insert)
connection.commit()
print(cursor.rowcount, "Record inserted successfully into Marvel table")

sql_select_Query = 'SELECT * FROM Marvel'
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

sql_delete_data = 'DELETE FROM Marvel WHERE Movie = "TheIncredibleHulk"'
cursor = connection.cursor()
cursor.execute(sql_delete_data)
dataBase.commit()

sql_select_phase2 = 'SELECT FROM Marvel WHERE MCU_Phase = "Phase2"'
cursor = connection.cursor()
cursor.execute(sql_select_phase2)
records = cursor.fetchall()

sql_query_update = 'UPDATE Marvel SET Date = "2017" WHERE Movie = "Thor:Ragnarok"'
cursor = connection.cursor()
cursor.execute(sql_query_update)
dataBase.commit()