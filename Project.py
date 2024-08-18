                   #PASSWORD MANAGER (MOST ADVANCED)#

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def get_fernet(master_pwd):
    key = load_key()
    combined_key = Fernet.generate_key()[:len(key)]  # Ensure key length matches
    return Fernet(key)

master_pwd = input("What is the master password? ")
fer = get_fernet(master_pwd)

def view():
    with open('Passwords.txt', 'r') as f:
        for line in f.readlines():
            user, passw = line.rstrip().split("|")
            print(f"User: {user} | Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('Passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input.")
        continue