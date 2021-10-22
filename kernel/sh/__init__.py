import os
import sys
import base64
import getpass
import platform
import pathlib
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import readline
import importlib

def get_user_key():
    keyfile = open("usr/secret.key", 'rb')
    key = keyfile.read()
    keyfile.close()
    return key

def read_user_pass():
    passfile = open("usr/password.key", 'rb')
    passw = passfile.read()
    passfile.close()
    return passw

def get_string_pass():
    f = Fernet(get_user_key())

    decrypted = decrypted = f.decrypt(read_user_pass()).decode()
    return decrypted


def start():
    print("KTerminal 1.0 - Rewrite")
    # salt = b'\xaf\xdb\xa2Z]\x99E{p\x1c\x14\xc6\xea\xc9B%'
    # kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
    # length=32,
    # salt=salt
    # ,
    # iterations=100000,
    # backend=default_backend())

    # key = base64.urlsafe_b64encode(kdf.derive(b"USER_KEY"))
    # file = open("usr/secret.key", 'wb')
    # file.write(key)
    # file.close()
    while True:
        workingdir = os.getcwd()
        strg = input(getpass.getuser() + "@" + platform.node() + workingdir + ":$ ")
        argv = strg.split(" ")
        argc = len(argv)
        if (argv[0] == "cd"):
            if len(argv) > 1:
                os.chdir(argv[1])
        elif argv[0] == "passwd":
            if pathlib.Path("usr/password.key").exists():
                print("replacing password")
                password = getpass.getpass("old password: ")
            else:
                password = getpass.getpass("new password: ")
                verify = getpass.getpass("verify password: ")
                if (password == verify):
                    print("password created")
                    passwordf = open("usr/password.key", 'wb')
                    f = Fernet(get_user_key())
                    encr = f.encrypt(password.encode())
                    passwordf.write(encr)
                    passwordf.close()
                      
        elif argv[0] == "test-superuser":
            passw = getpass.getpass("get pass for " + getpass.getuser() + ": ")
            f = Fernet(get_user_key())

            decrypted = decrypted = f.decrypt(read_user_pass()).decode()

            if passw == str(decrypted):
                print("you are superuser")
        else:
            if importlib.import_module("usr.bin." + argv[0]).main == None:
                if os.system(strg) != 0:
                    print("command not found.")
                else:
                    print(end="")
            else:
                importlib.import_module("usr.bin." + argv[0]).main(argc, argv)
        

