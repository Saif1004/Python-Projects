#!/usr/bin/env python3
import sys

from getpass import getpass

def adduser():
    usernames = []
    x = False
    print("Press Enter if you wish to stop adding users"'\n')
    while x == False:
        with open("passwd.txt", "a+") as myfile:
            user_name = input("Enter new username: ")
            if user_name in usernames:
                x = False
                print("Already in use")
                continue
            elif user_name == '':
                x = True
                myfile.close()
                print("DONE")
                break
            else:
                usernames.append(user_name)
            real_name = input("Enter real name: ")
            password = (getpass)("Enter your password: ")
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
            myfile.writelines([f"{user_name}:{real_name}:{combined}"])
            myfile.write('\n')
            print("User Created"'\n')


if __name__ == '__main__':
    adduser()
