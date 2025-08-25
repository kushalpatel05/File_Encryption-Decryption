from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)

        new_filename = filename + ".encrypted"
        with open(new_filename, "wb") as file:
            file.write(encrypted_data)

        print(f"✅ File encrypted successfully! Saved as {new_filename}")
    except FileNotFoundError:
        print("❌ Error: File not found.")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        if filename.endswith(".encrypted"):
            new_filename = filename.replace(".encrypted", ".decrypted.txt")
        else:
            new_filename = filename + ".decrypted.txt"

        with open(new_filename, "wb") as file:
            file.write(decrypted_data)

        print(f"✅ File decrypted successfully! Saved as {new_filename}")
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")

# Command-line menu
def menu():
    while True:
        print("\n--- File Encryptor & Decryptor ---")
        print("1. Encrypt a File")
        print("2. Decrypt a File")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            filename = input("Enter the filename to encrypt: ")
            encrypt_file(filename)
        elif choice == "2":
            filename = input("Enter the filename to decrypt: ")
            decrypt_file(filename)
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter 1-3.")

if __name__ == "__main__":
    menu()
