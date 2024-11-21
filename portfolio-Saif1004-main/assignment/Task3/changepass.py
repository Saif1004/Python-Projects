#!/usr/bin/env python3
import sys

from getpass import getpass


def changepass():
    x = False
    while x == False:
        with open("passwd.txt", "r+") as myfile:
            data = myfile.readlines()
            data = list(data)
            data = data[0]
            data = data.split(':')
            data[-1] = data[-1].strip()
            username = data[0]
            passwords = data[2]
            user_name = input("User: ")
            if user_name == username:
                print("Found")
            elif user_name != username:
                x = False
                print("Incorrect Username")
                continue
            password = (getpass)("Current Password: ")
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

            if combined == passwords:
                print("Correct")
                new_password = (getpass)("Enter New Password: ")
                new_password = new_password.strip(" ")
                encoded_password1 = []

                lower_list1 = []
                upper_list1 = []

                for x in range(0, 26):
                    upper_list1.append(chr(65 + x))
                    lower_list1.append(chr(97 + x))

                encoded_password1 = []
                for letter1 in new_password:
                    if letter1 in lower_list1:
                        if ord(letter1) + 13 > ord("z"):
                            encoded_password1.append(chr((ord(letter1) + 13) - 26))
                        else:
                            encoded_password1.append(chr(ord(letter1) + 13))
                    elif letter1 in upper_list1:
                        if ord(letter1) + 13 > ord("Z"):
                            encoded_password1.append(chr((ord(letter1) + 13) - 26))
                        else:
                            encoded_password1.append(chr(ord(letter1) + 13))
                    else:
                        encoded_password1.append(letter1)

                combined1 = "".join(encoded_password1)
                with open("passwd.txt") as myfile:
                    contents = myfile.read()
                    contents = contents.replace(passwords,combined1)
                with open("passwd.txt", 'w+') as myfile:
                    myfile.write(contents)


changepass()