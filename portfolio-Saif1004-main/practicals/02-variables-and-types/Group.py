#!/usr/bin/env python3

if __name__ == '__main__':


    students = int(input("How many students are there? "))
    group_size = int(input("What is the required group size? "))
    groups_needed = int(students/group_size)
    left_over = students % group_size
    print(f"There will be {groups_needed} groups needed and {left_over} students left over")



