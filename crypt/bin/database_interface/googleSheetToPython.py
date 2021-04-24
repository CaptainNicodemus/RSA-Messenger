# import library
import gspread
import pandas as pd
from datetime import datetime
# Service client credential from oauth2client
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('RSA Project-26ab4b3e3fbb.json', scope)
# authorize the clientsheet
client = gspread.authorize(creds)
# get the instance of the Spreadsheet
# sheet url
# https://docs.google.com/spreadsheets/d/184i1rPt7J_WIB0jttxDaZ8WdBq5JD42p9oeAnmK9Leg/edit#gid=0
sheet = client.open('Vulcans_RSA_Project')
# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


def add_message(sender_pubkey, encrypted_messageR, encrypted_messageS, receiver_pubKey):
    sheet_instance.append_row(
        [get_time_and_date(), sender_pubkey, receiver_pubKey, encrypted_messageR, encrypted_messageS])
    return


def get_time_and_date():
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %I:%M %p")
    return dt_string


def user_name_update(pubkey, new_username):
    sheet_instance.append_row([get_time_and_date(), pubkey, "", "", "", new_username])
    return
