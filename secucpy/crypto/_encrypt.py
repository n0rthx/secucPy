from cryptography.fernet import Fernet


def encrypt_fernet(call_msg_pakcage:str):

    key = Fernet.generate_key()
    fernet = Fernet(key)
    data = fernet.encrypt(call_msg_pakcage)

    return data

