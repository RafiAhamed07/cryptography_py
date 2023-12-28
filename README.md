# cryptography_py

This repository contains Python code demonstrating encryption and decryption using the Fernet symmetric key cryptography library from the cryptography package.

## Encryption (Code Block 1)

### Description:

The encryption script generates a random key, saves it to a file named "key.txt," and then encrypts a user-provided message using the generated key.

### Usage:

1. Run `encryption.py`.
2. Enter the message you want to encrypt when prompted.
3. The encrypted message and the generated key will be displayed.

## Decryption (Code Block 2)

### Description:

The decryption script reads the key from the "key.txt" file, prompts the user for a message and key, and then decrypts the message using the provided key.

### Usage:

1. Run `decryption.py`.
2. Enter the message you want to decrypt and the key when prompted.
3. The decrypted message will be displayed if the key is valid; otherwise, an error message will be shown.

## Prerequisites:

- Python 3.x
- cryptography library (`pip install cryptography`)

## File Structure:

- `encryption.py`: Contains the code for encrypting a message.
- `decryption.py`: Contains the code for decrypting a message.
- `key.txt`: Stores the randomly generated key for decryption.

## Notes:

- Ensure the cryptography library is installed (`pip install cryptography`).
- The key is crucial for decryption; keep it secure and do not share it.

Feel free to use this code as a reference or integrate it into your project as needed. If you encounter any issues or have questions, please refer to the documentation or open an issue in this repository.

