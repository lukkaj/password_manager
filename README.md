# password_manager
Simple terminal based password manager which utilizes sqlite as database. 

Password manager consist of main.py, menu.py, db_ops.py and encryption_ops.py.
Main is is the login menu where users can login with existing account, create account for password manager or just quit. Masterpassword is utilized in login. In menu users can decide wheater they want to for example store or retrieve stored passwords, there are also a few functions where different operations are performed. In db_ops (database operations) all actions towards database are performed. In encryption_ops (encryption operations) masterpassword can be hashed and checked if given password matches with hashed one, key's are generated to encrypt and decrypt application specific passwords. 


SQL database consists of two tables, Users and PWManaager.
  -Users: id, master password, email and key for decryption.
  -PWManager: id, app, email, password and user_id

Hashing + salt is used to conceal masterpassword. Other passwords are hidden with encryption. Decryption is handeld with user specific key.

Password manager can hold multiple users, users can log in and log out. When user is signed in
they can store new password for certain application or site, which will be encrypted and stored to sqlite database, update existing passwords, delete existing passwords, print one certain password as a table and print all of the stored information as a table. 

Before printing passwords those are decrypted.

To do:
  -GUI
  -Database design improvements
  -Increasing security
  
NOTE:
This passwords manager is not intended for actual use. Please use well-tested and trusted password managers to store your passwords.
