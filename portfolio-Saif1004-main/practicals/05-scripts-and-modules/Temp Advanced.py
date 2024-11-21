def fahrenheit_to_celcius(f):
    return (f-32)/2




if __name__ == '__main__':
    temperatures = []
    loop = -1
    while True:
        temp = input(f"Enter temp followed by F or C (e.g 10c) {loop +1}: ")
        loop += 1
        if temp == '':
            break
        unit = temp[-1]
        temp = temp[:-1]
        temp = int(temp)
        print(temp)
        print(unit)
        if unit == "F":
            temp = fahrenheit_to_celcius(temp)
            print(f"The temperature is {temp}C")
        temperatures.append(temp)
        print(temperatures)

maximum_temp = max(temperatures)
print(f"The highest temperature is {maximum_temp}")
minimum_temp = min(temperatures)
print(f"The lowest temperature is {minimum_temp}")
average_temp = sum(temperatures)/loop
print(f"The average temperature is {average_temp}")















