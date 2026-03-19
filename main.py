from cryptography.fernet import Fernet

def write_key():
    """Generate a key and save it to key.key — run only once!"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from key.key"""
    with open("key.key", "rb") as key_file:
        return key_file.read()

def view_passwords(fernet):
    """View all stored passwords"""
    try:
        with open('passwords.txt', 'r') as password_file:
            lines = password_file.readlines()
            if not lines:
                print("No passwords found. Add some first!")
                return
            for line in lines:
                user, encrypted_password = line.strip().split("|")
                decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                print(f"User: {user} | Password: {decrypted_password}")
    except FileNotFoundError:
        print("No passwords found. Add some first!")

def add_password(fernet):
    """Add a new encrypted password"""
    account_name = input('Account Name: ')
    password = input('Password: ')
    encrypted_password = fernet.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as password_file:
        password_file.write(f"{account_name}|{encrypted_password}\n")
    print(f"Password for '{account_name}' saved successfully!")

def main():
    # Uncomment the line below and run ONCE to generate your key
    # write_key()

    key = load_key()
    fernet = Fernet(key)

    while True:
        mode = input("\nWould you like to add a new password or view existing ones (view, add)? Press q to quit: ").lower()
        if mode == "q":
            print("Goodbye!")
            break
        elif mode == "view":
            view_passwords(fernet)
        elif mode == "add":
            add_password(fernet)
        else:
            print("Invalid mode. Please choose 'view', 'add', or 'q' to quit.")

if __name__ == "__main__":
    main()
