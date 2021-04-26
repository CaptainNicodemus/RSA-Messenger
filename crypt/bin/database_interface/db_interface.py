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

# Search for a username based on pubKey
def key_name_search(pubKey):

def get_message_table():
def get_names_table():