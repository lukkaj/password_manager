#!/usr/bin/env python
# Password manager main function
import menu, db_ops as db, getpass


def main():
    db.check_tables()
    checker = 0
    while checker == 0:
        login = input("Type 1 to login, 2 to signup or Q to quit ")
        if login == '1':
            email = input("Type your email address: ")
            password = getpass.getpass("Type your password: ")
            user_db = db.Database(email)
            m_pw = user_db.password_check(password)
            if m_pw == password:
                menu.menu(user_db)
            else:
                print("Given username or password is incorrect")
        elif login == '2':
            print("Create new account")
            menu.signup()
        elif login == 'Q':
            print("Thank you for using the password manager")
            checker = 1
            exit(0)
        else:
            print("Error, please try again")
 
    

if __name__ == '__main__':
    main()
