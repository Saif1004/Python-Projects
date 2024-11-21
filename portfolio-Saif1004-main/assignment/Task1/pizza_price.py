#!/usr/bin/env python3
import sys
import profile

def quantity():
    x = False
    while (x == False):
        try:
            pizza_number = int(input("How many pizzas are there? "))
            if pizza_number < 1:
                x = False
                print("Please enter a number higher than 0")
            else:
                x = True
                return pizza_number
        except ValueError:
            print("Please enter a whole number")

def delivery():
    t = False
    while (t == False):
        try:
            delivery = (input("Is delivery required? Enter y or n "))
            if delivery == 'y' and pizza_number > 4:
                delivery = 0
                print(f"Delivery is £{delivery:.2f}")
                return delivery
            elif delivery == 'n':
                if pizza_number > 4:
                    delivery = 0
                    print(f"Delivery is £{delivery:.2f}")
                    return delivery
                else:
                    delivery = 0
                    return delivery
            else:
                delivery = 2.50
                print(f"Delivery is £{delivery:.2f}")
                return delivery
        except ValueError:
            print("Please enter y or n! ")

def discount():
    m = False
    while (m == False):
        try:
            discount_cost = (input("Is it a Tuesday? Please enter with y or n "))
            if discount_cost == 'y':
                discount_cost = icost/2
                return discount_cost
            elif discount_cost == 'n':
                discount_cost = icost
                return discount_cost
        except ValueError:
            print("Please enter y or n! ")

def appuse():
    l = False
    cost = delivery + discount
    while (l == False):
        try:
            app = (input("Did the customer order through the app? Answer with y or n "))
            if app == 'y':
                cost = cost * 0.75
                print(f"The final price is £{cost:.2f}")
                return cost
            elif app == 'n':
                print(f"The final cost is £{cost:.2f}")
                return cost
        except ValueError:
            print("Error. Try again")


if __name__ == '__main__':
    pizza_number = quantity()
    icost = pizza_number * 12
    delivery = delivery()
    discount = discount()
    cost = delivery + discount
    appuse()


















