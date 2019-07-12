#TheFoodPlace.py
#by Adam Seidu
# A food orderning program which displays the menu to customers and allows them to choose their respective item codes with diffrent functions.

#import statements, Import any libraries which can help in the program structure

#Welcome To The Food Place!!!!!!!
#View Items
#View Prices
#Choose one or more items
#Increase Quantity Of Items
#View items and Price In Cart
#Place Order
#Enter Payment Information Inclding Email Address
#Confirm Order
#Generate Receipt
#Display Receipt
#Mail Receipt To Buyer
#Generate Profit Analysis Repor

import random

shopping_basket = {} #Initialize the shopping basket

print("Hello Buddy, Welcome To The Food Place!!!")

FOOD = {1 : "French Fries 5.25",
        2 : "1/4 pound Burger",
        3 : "1/2 pound Burger",
        4 : "1/4 pound CheeseBurger",
        5 : "1/2 pound CheeseBurger",
        6 : "Medium Pizza",
        7 : "Medium Pizza with Extra Topppings",
        8 : "Large Pizza",
        9 : "Large Pizza with Extra Toppings",
        10 : "Garlic Bread"
        }

print("""
FOOD PLACE OPTIONS
------------------
1:Select Food Item
2:Remove Food Item
3:View Chosen Food Items
0:Exit Program

""")



option = int(input("Enter an option: "))

while option != 0:
        if option == 1:
            for key,val in FOOD.items():
                print(key, "->", val)
            item = input("Enter a Food Item Number: ")
            qnty = int(input("Enter the quantity desired: "))
            shopping_basket[item] = qnty

        elif option == 2:
            item = input("Enter an item: ")
            del(shopping_basket[item])

        elif option == 3:
            for item in shopping_basket:
                print(item, ":",shopping_basket[item])

        elif option != 0:
            print("Invalid Response.")

        option = int(input("\n\nEnter an option: "))

else:
    print("Food Place Menu Closed.")
#input("\nPress enter to see a list of your options.")



