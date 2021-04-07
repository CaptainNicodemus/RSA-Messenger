import pyodbc

server = 'trey.database.windows.net'
database = 'Vulcancrypter'
username = 'trey'
password = 'Vulcanproject2021'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()


cursor.execute("SELECT TOP (1000) [id] ,[first_name] ,[last_name] ,[create_date] ,[is_active] FROM [dbo].[user]")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

count = cursor.execute("INSERT INTO [dbo].[user] ([id] ,[first_name] ,[last_name] ,[create_date] ,[is_active]) VALUES ('12', 'Python' , 'Test' , '2021-04-07', '1')")
cnxn.commit()
print('Rows inserted: ' + str(count))

cursor.execute("SELECT TOP (1000) [id] ,[first_name] ,[last_name] ,[create_date] ,[is_active] FROM [dbo].[user]")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()