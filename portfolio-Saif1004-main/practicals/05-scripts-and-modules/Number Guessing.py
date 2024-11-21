import random

def guess(x):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    random_number = random.choice(primes)
    tries = 0
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number: "))
        tries += 1
        print(f"Your number of tries is {tries}")
        if guess> random_number:
            print(f" {guess} is too high. Try again.")
        if guess< random_number:
            print(f" {guess} is too low")
        if tries>= 10:
            print("You have run out of guesses and lost.")
            return


    print(f"{guess} is correct")

guess(100)