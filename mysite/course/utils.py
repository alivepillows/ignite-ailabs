from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(value):
    encrypted_value = cipher_suite.encrypt(str(value).encode())
    return encrypted_value

def decrypt(encrypted_value):
    decrypted_value = cipher_suite.decrypt(encrypted_value).decode()
    return decrypted_value
