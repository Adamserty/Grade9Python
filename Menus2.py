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
#Generate Profit Analysis Report

import random

shopping_basket = {} #Initialize the shopping basket
price = {} #Initialize Price
total_price = 0 #Initialize total price
FriesPrice = 2.00
QuarterPoundPrice = 5.00
HalfPoundPrice  = 5.55
QuarterPoundCheesePrice = 7.00
HalfPoundCheesePrice = 7.50
MediumPizzaPrice = 9.00
MediumPizzaExtraPrice = 11.00
LargePizzaPrice = 12.00
LargePizzaExtraPrice = 14.50
GarlicPrice = 4.50

print("Hello Buddy, Welcome To The Food Place!!!")

FOOD = {1 : "French Fries" ,
        "FriesPrice" : "$2.00" ,
        2 : "1/4 pound Burger",
        "QuarterPoundPrice": "$5.00" , 
        3 : "1/2 pound Burger",
        "HalfPoundPrice" : "$5.55" ,
        4 : "1/4 pound CheeseBurger",
        "QuarterPoundCheesePrice" : "$7.00" ,
        5 : "1/2 pound CheeseBurger",
        "HalfPoundCheesePrice" : "$7.50" ,
        6 : "Medium Pizza",
        "MediumPizzaPrice" : "$9.00" ,
        7 : "Medium Pizza with Extra Topppings",
        "MediumPizzaExtraPrice" : "$11.00" ,
        8 : "Large Pizza",
        "LargePizzaPrice" : "$12.00" ,
        9 : "Large Pizza with Extra Toppings",
        "LargePizzaExtraPrice" : "$14.50" ,
        10 : "Garlic Bread",
        "GarlicPrice" : "$4.50" 
        }

print("""
FOOD PLACE OPTIONS
------------------
1:Select Food Item
2:Remove Food Item
3:View Chosen Food Items
4:View Total Price and Profit Percentage
0:Exit Program

""")

    
            

option = int(input("Enter an option: "))

while option != 0:
        if option == 1:
            for key,val in FOOD.items():
                print(key, "->", val)
            item = input("Enter a Food Item Number: ")
            item1 = int(input("Enter Price of Food Item "))
            qnty = int(input("Enter the quantity desired: "))
            shopping_basket[item] = qnty
            price = item1 * qnty
            total_price = int(total_price) + int(price)    
            percent = 0.1 * total_price
            
            

        elif option == 2:
            item = input("Enter an item: ")
            del(shopping_basket[item])

        elif option == 3:
            for item in shopping_basket:
                print(item, ":",shopping_basket[item])

        elif option == 4:
                print("Total Price In Basket : $" + str(total_price) + ".00")
                print("Profit is : $" + str(percent))
                                      
        elif option != 0:
                print("Invalid Response.")

        option = int(input("\n\nEnter an option: "))

else:
    print("Food Place Menu Closed.")
#input("\nPress enter to see a list of your options.")



