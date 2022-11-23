from cryptography.fernet import Fernet

'''
def write_key(): 
    key = Fernet.generate_key()
    #wb stands for write byte mode 
    with open("key.key", "wb") as key_file: 
        key_file.write(key)

write_key()
''' 

def load_key(): 
    file = open("key.key", "rb") 
    key = file.read() 
    file.close() 
    return key

# master_pwd = input("What is the master password?") 
# key = load_key() + master_pwd.encode() 
key = load_key()
fer = Fernet(key)

def view(): 
    with open("password.txt", 'r') as f: 
        for line in f.readlines(): 
            #rstrip helps to delete any whitespace at the end of the string
            data = line.rstrip() 
            user, passw = data.split(' | ') 
            print("User: ", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add(): 
    name = input("Account name: ") 
    pwd = input("Password: ") 
    
    #with in python will automatically close the file
    with open("password.txt", 'a') as f: 
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n") 


while True: 
    mode = input("Would you like to add a new password or view the existing one (add/view)?, press q to quit ").lower() 
    if mode == "q": 
        break; 
    
    if mode == "add": 
        add() 
    elif mode == "view":
        view()
    else: 
        print("Invalid mode.") 
        continue 
