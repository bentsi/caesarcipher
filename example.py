from caesarcipher.encrypt import encrypt
from caesarcipher.decrypt import decrypt


if __name__ == '__main__':
    cipher_step = 10
    encrypted_message = encrypt(text="verycool", step=cipher_step)
    print(f"Encrypted text: {encrypted_message}")
    decrypted_text = decrypt(encrypted_text=encrypted_message, step=cipher_step)
    print(f"Decrypted text: {decrypted_text}")
