#!/usr/bin/env python3
import re
import sys


filenames = sys.argv[1:]
for filename in filenames:
    file = open(str(filename), 'r')
    day_1 = file.readlines()


def cat_days():
    word = 'OURS'
    word2 = 'THEIRS'
    count = 0
    count1 = 0
    for line in day_1:
        words = line.split()
        for i in words:
            if i[0:4] == word:
                count = count + 1
    print(f"Cat Visits: {count}")
    for line in day_1:
        words = line.split()
        for i in words:
            if i[0:6] == word2:
                count1 = count1 + 1
    print(f"Other cats: {count1}\n")
    times = []
    for line in day_1:
        words = line.split()
        for i in words:
            if i[0:4] == word:
                temp = re.findall(r'\d+', line)
                res = list(map(int, temp))
                time = 0
                x = False
                while (x == False):
                        time1 = res[1] - res[0]
                        time += time1 + time
                        times.append(time)
                        x = True
    Hours = sum(times) // 60
    Minutes = sum(times) % 60
    Average = sum(times) / len(times)
    Longest = max(times)
    Shortest = min(times)
    print(f"Total Time in House: {Hours} Hours and {Minutes} Minutes \n")
    print(f"Average Visit Length: {Average:.0f} Minutes")
    print(f"Longest Visit Length: {Longest:.0f} Minutes")
    print(f"Shortest Visit Length {Shortest:.0f} Minutes \n")


if __name__ == '__main__':
    cat_days()
