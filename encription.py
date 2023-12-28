from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("key.txt", "wb") as f1:
    f1.write(key)

f = Fernet(key)

message = input("Enter message you want to encrypt:")

encrypted_msg = f.encrypt(message.encode())

e_msg = encrypted_msg.decode('latin-1')
k = key.decode('latin-1')
print("Encrypted message is:", e_msg)
print("Your key is:", k)
