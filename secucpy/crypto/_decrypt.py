from cryptography.fernet import Fernet 

def decrypt_fernet(key = Fernet.generate_key(), msg:str=None):


    # fernet decrypt method

    fernet = Fernet(key)

    return fernet.decrypt(msg)
