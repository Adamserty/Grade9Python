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
OPTIONS =  """
    Food Place Menu
-------------------------
1 : Select Food Item
2 : Remove Food Item
3 : View Chosen Food Items
4 : View Total Price And Profit
0 : Exit Program
"""

print("Hello Buddy, Welcome To The Food Place!!!")

FOOD = {1 : "French Fries" ,
        "FriesPrice" : "2.00" ,
        2 : "1/4 pound Burger",
        "QuarterPoundPrice": "5.00" , 
        3 : "1/2 pound Burger",
        "HalfPoundPrice" : "5.55" ,
        4 : "1/4 pound CheeseBurger",
        "QuarterPoundCheesePrice" : "7.00" ,
        5 : "1/2 pound CheeseBurger",
        "HalfPoundCheesePrice" : "7.50" ,
        6 : "Medium Pizza",
        "MediumPizzaPrice" : "9.00" ,
        7 : "Medium Pizza with Extra Topppings",
        "MediumPizzaExtraPrice" : "11.00" ,
        8 : "Large Pizza",
        "LargePizzaPrice" : "12.00" ,
        9 : "Large Pizza with Extra Toppings",
        "LargePizzaExtraPrice" : "14.50" ,
        10 : "Garlic Bread",
        "GarlicPrice" : "4.50" 
        }

myFOODvalues = FOOD.values()
myFOODvalues2 = list(myFOODvalues)
myFOODkeys = FOOD.keys()
myFOODkeys2 = list(myFOODkeys)
##myFOOD[0]
##{1 : "French Fries" ,
## 2 : "1/4 pound Burger",
## 3 : "1/2 pound Burger",
## 4 : "1/4 pound CheeseBurger",
## 5 : "1/2 pound CheeseBurger",
## 6 : "Medium Pizza",
## 7 : "Medium Pizza with Extra Topppings",
## 8 : "Large Pizza",
## 9 : "Large Pizza with Extra Toppings",
## 10 : "Garlic Bread"
##}
##
####myFOOD[1]
####{ FriesPrice : "$2.00" ,
####  QuarterPoundPrice: "$5.00" ,
####  HalfPoundPrice : "$5.55" ,
##  
##        
print(OPTIONS)


    
            

option = int(input("Enter an option: "))

while option != 0:
        if option == 1:
            for key,val in FOOD.items():
                print(key, "->", val)
            item = int(input("Enter a Food Item Number :"))
            if item <= 0:
                          print("Invalid Response")
                          print(OPTIONS)
                          continue

            elif item == 0:
                          print("Invalid Response")
                          print(OPTIONS)


            elif item > 10:
                          print("Invalid Response")
                          print(OPTIONS)
                          continue
                        
            qnty = int(input("Enter the quantity desired: "))
            price1 = float(myFOODvalues2[1])*qnty
            price2 = float(myFOODvalues2[3])*qnty
            price3 = float(myFOODvalues2[5])*qnty
            price4 = float(myFOODvalues2[7])*qnty
            price5 = float(myFOODvalues2[9])*qnty
            price6 = float(myFOODvalues2[11])*qnty
            price7 = float(myFOODvalues2[13])*qnty
            price8 = float(myFOODvalues2[15])*qnty
            price9 = float(myFOODvalues2[17])*qnty
            price10 = float(myFOODvalues2[19])*qnty
            if item == 1:
                        price2 = price2 - price2
                        price3 = price3 - price3
                        price4 = price4 - price4
                        price5 = price5 - price5
                        price6 = price6 - price6
                        price7 = price7 - price7
                        price8 = price8 - price8
                        price9 = price9 - price9
                        price10 = price10 - price10
                        print("Price is" + " " + str(price1))

            elif item == 2:
                          price1 = price1 - price1
                          price3 = price3 - price3
                          price4 = price4 - price4
                          price5 = price5 - price5
                          price6 = price6 - price6
                          price7 = price7 - price7
                          price8 = price8 - price8
                          price9 = price9 - price9
                          price10 = price10 - price10
                          print("Price is" + " " + str(price2))

            elif item == 3:
                         price1 = price1 - price1
                         price2 = price2 - price2
                         price4 = price4 - price4
                         price5 = price5 - price5
                         price6 = price6 - price6
                         price7 = price7 - price7
                         price8 = price8 - price8
                         price9 = price9 - price9
                         price10 = price10 - price10
                         print("Price is" + " " + str(price3))

            elif item == 4:
                          price1 = price1 - price1
                          price2 = price2 - price2
                          price3 = price3 - price3
                          price5 = price5 - price5
                          price6 = price6 - price6
                          price7 = price7 - price7
                          price8 = price8 - price8
                          price9 = price9 - price9
                          price10 = price10 - price10
                          print("Price is" + " " + str(price4))

            elif item == 5:
                         price1 = price1 - price1
                         price2 = price2 - price2
                         price3 = price3 - price3
                         price4 = price4 - price4
                         price6 = price6 - price6
                         price7 = price7 - price7
                         price8 = price8 - price8
                         price9 = price9 - price9
                         price10 = price10 - price10
                         print("Price is" + " " + str(price5))

            elif item == 6:
                          price1 = price1 - price1
                          price2 = price2 - price2
                          price3 = price3 - price3
                          price4 = price4 - price4
                          price5 = price5 - price5
                          price7 = price7 - price7
                          price8 = price8 - price8
                          price9 = price9 - price9
                          price10 = price10 - price10
                          print("Price is" + " " + str(price6))

            elif item == 7:
                          price1 = price1 - price1
                          price2 = price2 - price2
                          price3 = price3 - price3
                          price4 = price4 - price4
                          price5 = price5 - price5
                          price6 = price6 - price6
                          price8 = price8 - price8
                          price9 = price9 - price9
                          price10 = price10 - price10
                          print("Price is" + " " + str(price7))

            elif item == 8:
                          price1 = price1 - price1
                          price2 = price2 - price2
                          price3 = price3 - price3
                          price4 = price4 - price4
                          price5 = price5 - price5
                          price6 = price6 - price6
                          price7 = price7 - price7
                          price9 = price9 - price9
                          price10 = price10 - price10
                          print("Price is" + " " + str(price8))

            elif item == 9:
                          price1 = price1 - price1
                          price2 = price2 - price2
                          price3 = price3 - price3
                          price4 = price4 - price4
                          price5 = price5 - price5
                          price6 = price6 - price6
                          price7 = price7 - price7
                          price8 = price8 - price8
                          price10 = price10 - price10
                          print("Price is" + " " + str(price9))

            elif item == 10:
                          price1 = price1 - price1
                          price2 = price2 - price2
                          price3 = price3 - price3
                          price4 = price4 - price4
                          price5 = price5 - price5
                          price6 = price6 - price6
                          price7 = price7 - price7
                          price8 = price8 - price8
                          price9 = price9 - price9
                          print("Price is" + " " + str(price10))

            
            cent = float(input("Enter Profit Percentage As A Decimal :"))
            shopping_basket[item] = qnty
            price = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 + price9 + price10
            total_price = int(total_price) + int(price)    
            percent = cent * total_price
            print(OPTIONS)
            
            

        elif option == 2:
            item = input("Enter an item: ")
            del(shopping_basket[item])
            print(OPTIONS)

        elif option == 3:
            for item in shopping_basket:
                print(item, ":",shopping_basket[item])
                print(OPTIONS)

        elif option == 4:
                print("Total Price In Basket : $" + str(total_price) + ".00")
                print("Profit is : $" + str(percent))
                print(OPTIONS)
                                      
        elif option != 0:
                print("Invalid Response.")
                print(OPTIONS)

        elif str(option) == "":
                print("Invalid Response")
                print(OPTIONS)

        option = int(input("\n\nEnter an option: "))

else:
    print("Food Place Menu Closed.")
#input("\nPress enter to see a list of your options.")



