from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

ENCRYPTION_KEY = bytes.fromhex("00112233445566778899aabbccddeeff")  # Replace with your 32-byte encryption key
IV_LENGTH = 16  # For AES, this is always 16

def pad_data(data):
    block_size = AES.block_size
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length]) * padding_length
    return data + padding

def encrypt(text):
    iv = get_random_bytes(IV_LENGTH)
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_data(text.encode()))
    
    return binascii.hexlify(iv).decode() + ':' + binascii.hexlify(encrypted).decode()

def decrypt(encrypted_text):
    iv, encrypted = encrypted_text.split(':')
    iv = binascii.unhexlify(iv)
    encrypted = binascii.unhexlify(encrypted)
    
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    
    return decrypted.rstrip(b'\x00').decode()

def main():
    while True:
        print("Select an option:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            plaintext = input("Enter the text to encrypt: ")
            encrypted_text = encrypt(plaintext)
            print("Encrypted:", encrypted_text)
        elif choice == '2':
            encrypted_input = input("Enter the encrypted text: ")
            decrypted_text = decrypt(encrypted_input)
            print("Decrypted:", decrypted_text)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

