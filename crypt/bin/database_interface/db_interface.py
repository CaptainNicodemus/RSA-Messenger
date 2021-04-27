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
  # Use pandas boolean indexing to filter public keys
  my_messages = dataframe[(dataframe["Public Key Sender"] == pubKey) | (dataframe["Public Key Receiver"] == pubKey)]

  # Clean up the dataframe
  my_messages = my_messages.drop("Public Key Sender", 1)
  my_messages = my_messages.drop("Public Key Receiver", 1)
  return my_messages

# Search for a username based on pubKey
def key_name_search(pubKey):
  i = 1
  for key in dataframe['Public Key Sender']:
    if key == pubKey:
      if dataframe.loc[i, "Sender User Name"] == "-":
        continue
      else:
        return dataframe.loc[i, "Sender User Name"]
    i += 1

def time_sort():
  time_sorted = dataframe.sort_values(by="Time")
  return time_sorted

def name_sort():
  #sort by name
  return

def get_message_table():
  #
  return

def get_names_table():
  #
  return