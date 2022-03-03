# import library
import gspread
import pandas as pd
import os
from datetime import datetime

from pandas.core.computation import scope

credentials = {
    "type": "service_account",
    "project_id": "rsa-project-311701",
    "private_key_id": "26ab4b3e3fbb8c60c00cba5654314ecba5b9b63b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC2/plV8Q7pw0/A\n45CyqV0EbnaaTNWaBTBH0Ekxwu6vpEDCTcqG4Jqk/yo1lds9wpaGE/THPcQChYiU\nlgWhPuCkI2akZwf54Cty52s1L6k8I69Q1A6Ogu4T0+RM/wRbmOX+koCuC/kVruwT\nb7U4wuPO6b8+HurPjiVmzLyHelNbDnqOAh/SE4L1MtwmkvN8MTSeLNgUAtc8/1LT\nClDPJa/TN1KQemYsgQC8BR19ISB+PNjaLee8AyahNzE/NnQ3BDjUP6s7lHG+ABbu\nuLPJcZKhaFz0Q2X3xQZnT5IsLbfYRIUx0AD76vo8ViTp46P7VkqxiYi3dS4y1L1+\nDqju6W2dAgMBAAECggEADJR2w2sNn2cHNeIZscPlhRx4QtCYDpKKEyXFIl/y5gLg\nq3rgOrgjaXGxMSXa1eVpUPumOYbhfAWPXMeYyND4bdA7337Fvu5444P34XF5V40M\ndv4Hp3xmFC7eOad+YTL4UgaNmhQbTNui7GMi44K3rnhwkTtcNmXgjwScIU7OKYA4\n4f7Ue+u/1oYVIfo9GgVaMsO0UNRNhk7HLaYlyARZMs/VdnMOspsJU+ibK04FGHjc\ne7g8PFybzXenq/0xBPa/BBryv/VU8do8exeGHY9r8wywMuteczQVxPiIatDJDDWg\n1Q7UfeQxdWrlUn8tdwF8CeiD0LZ6sV+YGkKjx2nbcQKBgQDaicDCYFqtx+kyMH5+\nk+TxHBt0d0l51YRaHD4X0f2ydHHfEA16jpVmJqMSx5UItF0wHFTorG3nJ0ktcf7H\nloRsppengOxUB/HuNCW2xjEv/CclbjNSUw9XVyDfCOOaTXh47nyMa/zL54Nit0id\nWfkuunqUSUan9v/nVGl+WUQQawKBgQDWXRCVuwvhszOi/NvDYdUT2NvgqkAWaxmI\naRD4nqK7IEjh/AojIbk50c6V455nk3Dqnx+IiPtKRJ/Df/eFttzCPjZcW2tNtwLQ\nUJUxTXybLNUlqodmYYQn62H80MrEY7QMQwrJhrlpaPSyIfw7Fcs+7QbAFbZ5qmPK\nngLrbxDcFwKBgEkB2BmXovOHY4pW1QtoUQWThECGUU+YWxzXbo76oixp5ljEvhwB\nYju8EKKHdmxwBOm7rUoFwLmGUFYUTS9UQ20gwm09DraL6PDRDwBeebQ0IsfIZvDL\nusZM3zhjedXkp6iO06D9unhMIYJrBKE8m5hWx/id+jLGu3sGoi+Jlsl9AoGAN9+G\nBSD91dRZry/tMB395fBuTz7Q+Ybs3stT6xmeHNwrYwvIsKOHnfR7vkHX9fNOSTk0\nhOf/Z7o/Uju2jpm9LLv+e1Awxc7f4uA+It2pjuC+pdSu+haM1cLahYT+dPXv5gpL\nc3+0MC91KEEHd3cUxNAPJF4Ec+3fmN5asHcAk/0CgYBZ4AOA4y9Fi/Ut607T5Ja2\nZAoay+YcutfHNa0In2Om1d2a9s0hSDF7SJUvYw5g5+FSdeC/NrzqLk1PUvPZfAi9\nEZlqsqNFN4Xio87u6Vsbg0jC1FsyvMIamMHdBxir+gCDJwQ4fyk0kh42zkhA71oO\nncjNCWnF/6ogBJEyNarroA==\n-----END PRIVATE KEY-----\n",
    "client_email": "my-service-account@rsa-project-311701.iam.gserviceaccount.com",
    "client_id": "117985830335162214850",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-service-account%40rsa-project-311701.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open("Vulcans_RSA_Project")

sheet_instance = sh.get_worksheet(0)


def add_message(sender_pubkey, encrypted_messageR, encrypted_messageS, receiver_pubKey):
    sheet_instance.append_row(
        [get_time_and_date(), str(sender_pubkey), str(receiver_pubKey), str(encrypted_messageR), str(encrypted_messageS), "-"])
    return


def get_time_and_date():
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %I:%M %p")
    return dt_string


def add_user_name_update(pubkey, new_username):
    string = str(pubkey)
    sheet_instance.append_row([get_time_and_date(), string, "-", "-", "-", new_username])
    return


def get_all_val():
    list_of_lists = sheet_instance.get_all_values()
    return list_of_lists