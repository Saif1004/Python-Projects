#!/usr/bin/env python3
import re
import sys

from getpass import getpass

def loginuser():
    x = False
    while (x == False):
        with open('passwd.txt', 'r') as f:
            data = f.readlines()
            data = list(data)
            data = data[0]
            data = data.split(':')
            data[-1] = data[-1].strip()
            username = data[0]
            passwords = data[2]
            user = input("User: ")
            password = (getpass)("Password: ")
            password = password.strip(" ")
            encoded_password = []

            lower_list = []
            upper_list = []

            for i in range(0, 26):
                upper_list.append(chr(65 + i))
                lower_list.append(chr(97 + i))

            encoded_password = []
            for letter in password:
                if letter in lower_list:
                    if ord(letter) + 13 > ord("z"):
                        encoded_password.append(chr((ord(letter) + 13) - 26))
                    else:
                        encoded_password.append(chr(ord(letter) + 13))
                elif letter in upper_list:
                    if ord(letter) + 13 > ord("Z"):
                        encoded_password.append(chr((ord(letter) + 13) - 26))
                    else:
                        encoded_password.append(chr(ord(letter) + 13))
                else:
                    encoded_password.append(letter)

            combined = "".join(encoded_password)
        if user == username and combined == passwords:
            print("Access granted. ")
            x = True
            return user, password
        elif user != username and combined != combined:
            x = False
            print("Incorrect username or password ")
        else:
            x = False
            print("Incorrect. Please try again")


loginuser()
