# Database creation and operations
import sqlite3, getpass as getp, encryption_ops as enc


class Database:
    def __init__(self, email, database = "password.db"):
        self.email = email
        self.connect = sqlite3.connect(database)
        self.connect.isolation_level = None
        self.cursor_pw = self.connect.cursor()


    def execute(self, query, data):
        self.cursor_pw.execute(query, data)
        self.connect.commit()
        return self.cursor_pw


    def close_db(self):
        self.connect.close()


    def get_user_key(self):
            query = "SELECT U.key FROM Users U WHERE U.email = ?"
            key = self.execute(query, [self.email]).fetchone()[0]
            return key


    def insert_to_db(self, app, password):
        key = self.get_user_key()
        encrypted_password = enc.encrypt(key, password)
        query = "INSERT INTO PWManager (app, email, password) VALUES (?,?,?)"
        self.execute(query, [app, self.email, encrypted_password])
        

    def update_db(self, app, new_pw):
        key = self.get_user_key()
        encrypted_password = enc.encrypt(key, new_pw)
        query = "UPDATE PWManager SET password = ? WHERE email = ? AND app = ?"
        self.execute(query, [encrypted_password, self.email, app])


    def remove_from_db(self, app_name):
        query = "DELETE FROM PWManager WHERE email = ? AND app = ?"
        self.execute(query, [self.email, app_name])
     

    def password_check(self, password):
        try:
            query = "SELECT U.masterpw FROM Users U WHERE U.email = ?"
            master_password = self.execute(query, [self.email]).fetchone()[0]
            if enc.pw_unhash(password, master_password):
                print("Logged in succesfully")
                return password
            else:
                return False
        except:
            return False


    def app_search(self, app_name):
        try:
            query = "SELECT P.app FROM PWManager P WHERE P.email = ? AND P.app = ?"
            return self.execute(query, [self.email, app_name]).fetchone()[0]
        except:
            print("Empty")

    
    """
    Different security methods are used for passwords that need to be
    encrypted and not hashed. 
    """
    def get_password_one(self, app):
        try:
            key = self.get_user_key()
            query = "SELECT P.app, P.email, P.password FROM PWManager P WHERE P.email = ? AND P.app = ?"
            user_info = self.execute(query, [self.email, app]).fetchall()
            user_info = [list(info) for info in user_info]
            decrypted = enc.decrypt(key, user_info[0][2])
            user_info[0][2] = decrypted
            return user_info
        except:
            print("Empty")


    def get_password_all(self):
        try:
            key = self.get_user_key()
            query = "SELECT P.app, P.email, P.password FROM PWManager P WHERE P.email = ?"
            user_info = self.execute(query, [self.email]).fetchall()
            user_info = [list(info) for info in user_info]
            index = 0
            while index < len(user_info):
                user_info[index][2] = enc.decrypt(key, user_info[index][2])
                index += 1
            return user_info 
        except:
            print("No passwords to show")


"""
Users who are not signed to the service will use functions to create account.
Class Database is for registered users and therefore implements an registered
user when user signs in.
"""

def not_signed_connection():
    db = sqlite3.connect("password.db")
    db.isolation_level = None
    cursor = db.cursor()
    return cursor


def execute_not_signed(query, data):
    cursor_pw = not_signed_connection()
    cursor_pw.execute(query, data)
    sqlite3.connect("password.db").commit()
    return cursor_pw


def none_check(query):
    if query == None:
        return True
    else:
        return False


def check_tables():
        execute_not_signed("""
            CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE, 
            masterpw BLOB,
            key BLOB
            )""", [])

        execute_not_signed("""
            CREATE TABLE IF NOT EXISTS PWManager (
            id INTEGER PRIMARY KEY,
            app TEXT, 
            email TEXT, 
            password BLOB,
            user_id INTEGER REFERENCES Users (id))
            """, [])
        print("Welcome to password manager")


"""
Try to search emails that match with given email.
"""
def search_email_match(new_email):
        res = execute_not_signed("""
            SELECT U.email
            FROM Users U
            WHERE U.email == ?
            """, [new_email]).fetchone()
        if none_check(res) == True:
            return False
        else:
            return res[0]

"""
New users password will be hashed to increase security
"""

def new_user(new_email, new_password):
    try:
        execute_not_signed("""
            INSERT INTO Users (email, masterpw, key) 
            VALUES (?,?,?)""", 
            [new_email, enc.pw_hashing(new_password), enc.get_key()])
    except:
        print("Error")

    
      






















































