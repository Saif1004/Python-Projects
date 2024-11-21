#!/usr/bin/env python3
import sys

def deluser():
    file = open("passwd.txt","r")
    lines = file.readlines()
    usernames = lines[0]
    file.close()

    user_name = input("Enter your username: ")

    file = open("passwd.txt","w")
    for line in lines:
        if line.rstrip() == user_name:
            file.write(line)

    file.close()


deluser()
