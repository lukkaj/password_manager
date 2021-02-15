# Cryptorphy, hashing and all other secret stuff 
import bcrypt 
from cryptography.fernet import Fernet

"""
Hashing is used to conceal master password, other passwords are 
encrypted and those can be decrypted with the use of a user specific key.
"""
def pw_hashing(password):
	pw = password.encode()
	hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
	return hashed


def pw_unhash(input_pw, db_pw):
	pw = input_pw.encode()
	if bcrypt.checkpw(pw, db_pw):
		print("Password is correct")
		return True
	else:
		print("Invalid credentials")
		return False


def get_key():
	key = Fernet.generate_key()
	return key


def encrypt(key, password):
	f = Fernet(key)
	return f.encrypt(password.encode())


def decrypt(key, encrypted_pw):
	f = Fernet(key)
	pw = f.decrypt(encrypted_pw)
	return pw.decode()