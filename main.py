from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def view_passwords(fernet):
    try:
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No passwords found. Add some first!")
                return
            for line in lines:
                user, pwd = line.strip().split("|")
                print(f"User: {user} | Password: {fernet.decrypt(pwd.encode()).decode()}")
    except FileNotFoundError:
        print("No passwords found. Add some first!")

def add_password(fernet):
    name = input('Account Name: ')
    pwd = input('Password: ')
    enc = fernet.encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{enc}\n")
    print("Password saved!")

def main():
    write_key()
    key = load_key()
    fernet = Fernet(key)
    while True:
        mode = input("\nType view, add, or q to quit: ").lower()
        if mode == "q":
            print("Goodbye!")
            break
        elif mode == "view":
            view_passwords(fernet)
        elif mode == "add":
            add_password(fernet)
        else:
            print("Invalid. Try view, add or q.")

if __name__ == "__main__":
    main()
