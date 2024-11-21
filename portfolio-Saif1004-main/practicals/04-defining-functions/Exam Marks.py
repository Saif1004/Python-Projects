#!/usr/bin/env python3

import math

if __name__ == '__main__':
    marks = []
    x = False
    grades = []

    while (x == False):

        mark = (input("What mark would you like to enter: "))
        marks.append(mark)
        print(marks)

        if mark == "":
            print(grades)
            marks = marks[:-1]
            print(marks)
            break




        mark = int(mark)





        if mark > 70:
            grade = ("A")
            grades.append(grade)
            print(grades)
        if 70 > mark > 60:
            grade = ("B")
            grades.append(grade)
            print(grades)
        if 60 > mark > 50:
            grade = ("C")
            grades.append(grade)
            print(grades)
        if 50 > mark > 40:
            grade = ("D")
            grades.append(grade)
            print(grades)
        elif mark < 40:
            grade = ("F")
            grades.append(grade)
            print(grades)





























