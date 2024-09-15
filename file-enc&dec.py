# file encryption and decryption
# Symmetric encryption algorithms are generally used for encryption operations, but here we can use the Fernet encryption method as a basic example.

from cryptography.fernet import Fernet
import os

# key created and put in file
def create_key():
    return Fernet.generate_key()

def write_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# encryption
def file_encrypt(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_name + ".enc", "wb") as file:
        file.write(encrypted_data)
    print(f"{file_name} file is encrypted and {file_name}.enc was recorded as.")

# decryption
def file_decrypt(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_name.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)
    print(f"{file_name} The file is decrypted and {file_name.replace('.enc', '')} was recorded as.")

# creat key or load key
if not os.path.exists("key.key"):
    key = create_key()
    write_key(key)
else:
    key = load_key()

# user action 
action = input("Select Encryption (e) or Decryption (d) operation : ").lower()
file_name = input("Enter file name: ")

if action == 'e':
    file_encrypt(file_name, key)
elif action == 'd':
    if file_name.endswith(".enc"):
        file_decrypt(file_name, key)
    else:
        print("Enter a file with the .enc extension for decryption.")
else:
    print("Invalid selection.")