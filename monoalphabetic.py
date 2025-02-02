# Implementation of Monoalphabetic ciphertext
import string

def get_key_from_user():
    letters = string.ascii_lowercase
    print("Enter a 26-letter substitution key:")
    while True:
        user_key = input("Key: ").lower()
        if len(user_key) == 26 and set(user_key) == set(letters):
            return dict(zip(letters, user_key))
        else:
            print("Invalid key! Ensure it contains all 26 unique lowercase letters.")

def encrypt(text, key):
    encrypted_text = ""
    for char in text.lower():
        encrypted_text += key.get(char, char)  # Keep non-alphabet characters unchanged
    return encrypted_text.upper()

def decrypt(ciphertext, key, original_text):
    reversed_key = {value: key for key, value in key.items()}
    decrypted_text = ""
    for char in ciphertext.lower():
        decrypted_text += reversed_key.get(char, char)  # Keep non-alphabet characters unchanged
    
    # Restore original case
    restored_text = "".join(orig if not orig.isalpha() else decrypted_text[i] if orig.islower() else decrypted_text[i].upper()
                              for i, orig in enumerate(original_text))
    return restored_text

# Get user-defined key
key = get_key_from_user()

# Get plaintext from user
plaintext = input("Enter the plaintext: ")

# Encrypt and decrypt
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_message = decrypt(ciphertext, key, plaintext)
print(f"Regenerated Plaintext: {decrypted_message}")
