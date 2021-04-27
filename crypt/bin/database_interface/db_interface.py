import googleSheetToPython as gstp
import pandas as pd


class db_interface:
  
  # Constructor to get the table and set the columns
  def __init__(self):
      self.init_table = gstp.get_all_val()
      self.dataframe = pd.DataFrame(init_table)
      self.columns = dataframe[0]
      
  
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
   
     
    
    return #username

  def time_sort(dataframe):
      # unsure about dataframe
      parametersself.dataframe['Date'] = pd.to_datetime(self.dataframe.Date)
      sorted_df = self.dataframe.sort('Date')
      return sorted_df  # sort table by time

  def name_sort(dataframe):
      # sort by name
      # unsure about dataframe parameters
      name_sorted_dataframe = self.dataframe.sort_values(by=['Name'])
      return name_sorted_dataframe
    
  def get_message_table():
    #
    return
    
  def get_names_table():
    #
    return