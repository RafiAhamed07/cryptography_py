from cryptography.fernet import Fernet

with open("key.txt", "rb") as f2:
    key1 = f2.read()

msg = input("Enter the message you want to encrypt:")
key = input("Enter the Key:")
if key1 == key.encode():
    cipher_suite = Fernet(key)
    decrypted_msg = cipher_suite.decrypt(msg)
    d_msg = decrypted_msg.decode('latin-1')
    print(d_msg)
else:
    print("Key not valid")
