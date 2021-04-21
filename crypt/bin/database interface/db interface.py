import pyodbc

server = 'vulcans.database.windows.net'
database = 'Vulcancrypter'
username = 'vulcans'
password = 'Vulcanproject2021'

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


def user_add(user_name, public_key):
    # check if user_name already exists in database
    check_username = cursor.execute(
        'SELECT user_name FROM user WHERE user_name = %(username)s', (user_name,))
    check_username = cursor.fetchone()
    if check_username != 0:
        cursor.execute(
            "INSERT INTO [dbo].[user] ([user_name], [public_key]) VALUES (user_name, public_key)")
        print('User added')
    else:
        print('user_name already exists in database')


def user_login(user_name, public_key):
    check_login = cursor.execute(
        'SELECT user_name FROM user WHERE user_name = %(user_name)s, public_key = %(public_key)',
        (user_name, public_key))
    check_login = cursor.fetchone()
    if check_login != 0:
        print("Log in successful")
    else:
        print("User name or public key incorrect")
