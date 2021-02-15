# This is menu for the password manager
import db_ops as db, getpass as getp, pandas as pd, main

"""
In this file most user inputs are handled.
"""
def password_match():
    pw_condition = True
    while pw_condition:
        first_pw = getp.getpass("Enter new password: ")
        second_pw = getp.getpass("Enter password again: ")
        if first_pw == second_pw:
            pw_condition = False
            return first_pw
        else:
            print("Passwords did not match")    


def signup():
    rounds = 3
    counter = 0
    while counter < rounds:
        email = input("Please enter your email address or type Q to return to main menu: ")
        if email == 'Q':
            print("Back to main menu")
            break
        master_password  = password_match()
        choice = input("Is your email correct? yes or no: ")
        email_in_db = db.search_email_match(email)
        if email_in_db == email:
            print("Given email is already in use, sign in or use another email")
        elif email_in_db == False and choice == "yes": 
            db.new_user(email, master_password)
            print("Succesfully stored information")
            counter = 4
        elif choice == "no":
            print("Enter email again")


def store_new(user_db):
    print("Create new password for certain site or app")
    app_name = input("Enter site or app name: ")
    if user_db.app_search(app_name) != app_name:
        print("Continue to add password information")
        password = password_match()
        user_db.insert_to_db(app_name, password)
        print(f"Succesfully added {app_name}'s data")
    else:
        print(f"App {app_name} is already stored into database")


def update_pw(user_db):
    print("Update existing password")
    app_name = input("Enter site or app name: ")
    if user_db.app_search(app_name) == app_name:
        print("Continue to update password")
        password = password_match()
        user_db.update_db(app_name, password)
        print(f"Succesfully updated {app_name} password")
    else:
        print(f"There are no entries regarding {app_name}")


def delete_pw(user_db):
    print("Delete password from the database")
    app_name = input("Enter site or app name: ")
    if user_db.app_search(app_name) == app_name:
        user_db.remove_from_db(app_name)
        print(f"Succesfully deleted all data regarding {app_name}")
    else:
        print(f"No passwords regarding {app_name}")


def print_table(pw_list):
    pd.options.display.show_dimensions = False
    print(pd.DataFrame(pw_list, columns = ["App", "Email", "Password"]))


def print_one(user_db):
    print("Print one password from specific site or app")
    app_name = input("Enter site or app name: ")
    found_password = user_db.get_password_one(app_name)
    if not found_password:
        print(f"No saved passwords for {app_name}")
    else:
        print_table(found_password)


def print_all(user_db):
    print("Print table of all passwords")
    all_passwords = user_db.get_password_all()
    if not all_passwords:
        print("Empty")
    else:
        print_table(all_passwords)


def menu(user_db):
    choice = ""
    while choice != 'Q':
        print("""
        -------------------------------------------------------
        |                       Menu                          |
        -------------------------------------------------------
        |   1.) Store new password                            |
        |   2.) Update existing password                      |
        |   3.) Delete password from specific site/app        |
        |   4.) Get password of spesific site/app             |
        |   5.) Get table of all passwords                    |
        |   Q.) Log out                                       |
        -------------------------------------------------------
        """)
        choice = input("Your choice: ")
        if choice == '1':
            store_new(user_db)
        elif choice == '2':
            update_pw(user_db)
        elif choice == '3':
            delete_pw(user_db)
        elif choice == '4':
            print_one(user_db)
        elif choice == '5':
            print_all(user_db)
        elif choice == 'Q':
            user_db.close_db()
            print("Back to login menu")
        else:
            print("Wrong input")







    
    
