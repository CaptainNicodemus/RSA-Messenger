import pyodbc

server = 'vulcans.database.windows.net'
database = 'Vulcans'
username = 'vulcans'
password = 'Vulcanproject2021'

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


def user_add(user_name, public_key):
    # check if user_name already exists in database
    check_username = cursor.execute(
        'SELECT user_name FROM user WHERE user_name = %(public_key)s', (public_key,))
    check_username = cursor.fetchone()
    if check_username != 0:
        id = cursor.execute(
            'SELECT MAX id FROM user')
        id = cursor.fetchone()
        id = id + 1
        check_username = cursor.fetchone()
        cursor.execute(
            "INSERT INTO [dbo].[user] ([id],[user_name], [public_key]) VALUES (id, user_name, public_key)")
        print('User added')
    else:
        print('user_name already exists in database')


def user_login (public_key):
    check_login = cursor.execute(
        'SELECT user_name FROM user WHERE user_name = %(user_name)s, public_key = %(public_key)',
        (user_name, public_key))
    check_login = cursor.fetchone()
    if check_login != 0:
        print("Log in successful")
    else:
        print("User name or public key incorrect")

<<<<<<< HEAD
=======
def get_messages(public_key):

def send_messages(public_key):

def change_user_name(new_user_name, public_key):

    
>>>>>>> master
