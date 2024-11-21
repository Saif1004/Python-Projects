#!/usr/bin/env python3

if __name__ == '__main__':
    temperatures = []


    for temp in range(4):
        temp = (input("What is the temperature? (With Units) "))
        unit = temp[-1]
        temp = temp[:-1]
        temp = int(temp)

        if unit == "F":
            temp = (temp-32)*0.55555555555
            print(temp)

        temperatures.append(temp)
        print(temperatures)

    maximum_temp = max(temperatures)
    print(f"The highest temperature is {maximum_temp}")
    minimum_temp = min(temperatures)
    print(f"The lowest temperature is {minimum_temp}")
    average_temp = sum(temperatures)/4
    print(f"The average temperature is {average_temp}")









