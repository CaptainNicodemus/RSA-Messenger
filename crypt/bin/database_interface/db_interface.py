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