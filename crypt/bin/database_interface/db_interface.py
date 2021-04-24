from bin.database_interface.googleSheetToPython import add_user_name_update, add_message


def send_message(sender_pubkey, encrypted_messageR, encrypted_messageS, receiver_pubKey):
    add_message(sender_pubkey, encrypted_messageR, encrypted_messageS, receiver_pubKey)
    return

def user_name_update(pubKey, new_username):
    add_user_name_update(pubKey, new_username)
    return

def pull_message(pubKey):
    my_messages = 0
    return my_messages





# def message_search(message):
#   while True
#
#
# def populate_cell(message):
#   i = 1
#   j = 1
#   while True:
#     cell = sheet.cell(i,j)
#     if cell is not None:
#       sheet.update_cell(i, j, message)
#       return True
#     i++
