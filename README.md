# password_manager
Simple terminal based password manager which utilizes sqlite as database. 

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
