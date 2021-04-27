import pandas

import googleSheetToPython as gstp
import pandas as pd


# Setting up the dataframe
init_table = gstp.get_all_val()
dataframe = pd.DataFrame(init_table)
dataframe = dataframe.rename(columns={0: 'Time', 1: 'Public Key Sender', 2: 'Public Key Receiver', 3: 'MessageR',
                          4: 'MessageS', 5: 'Sender User Name'})
dataframe = dataframe.drop(0)

def send_message(sender_pubkey, encrypted_messageR, encrypted_messageS, receiver_pubKey):
  gstp.add_message(sender_pubkey, encrypted_messageR, encrypted_messageS, receiver_pubKey)
  return

def user_name_update(pubKey, new_username):
  gstp.add_user_name_update(pubKey, new_username)
  return

def pull_message(pubKey):
  my_messages = key_name_search(pubKey)
  return my_messages

# Search for a username based on pubKey
def key_name_search(pubKey):
  i = 0
  for key in dataframe['1']:
    if key == pubKey:
      return dataframe.iloc['5', i]
    i += 1

def get_messages(pubKey):
  messages = pandas.DataFrame
  messages.columns = ["Time", "Received", "Sent"]

  sent_messages = pd.DataFrame(dataframe.loc[dataframe['Public Key Sender'] == pubKey])

  print(sent_messages)

  received_messages = pd.DataFrame(dataframe.loc[dataframe['Public Key Receiver'] == pubKey])

  print(received_messages)

def time_sort():
  #sort table by time
  return

def name_sort():
  #sort by name
  return

def get_message_table():
  #
  return

def get_names_table():
  #
  return