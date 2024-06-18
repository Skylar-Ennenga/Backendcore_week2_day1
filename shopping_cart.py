# create a shopping garage application that adds items to a shopping garage (a dictionary)
# the key will be the item, the value will be the price

# shopping_garage = {}

# def add_item(garage):
#     # store the item as a key
#     item = input("What would you like to add to your garage?")
#     # taking quantity and price so we can see how much that number of items costs
#     quantity = int(input(f"How many of {item} would you like? "))
#     price = float(input(f"How much does {item} cost? "))
#     # total price as a value
#     total_item_price = quantity * price

#     # gives our dictionary a key of the item and a value of the price * quantity
#     garage[item] = total_item_price

# def remove_item(garage):
#     item = input("What would you like to remove from your garage? ")
#     # checking if our item is not in the garage
#     if item not in garage:
#         # if its not telling the user the item doesnt exist
#         print("You dont have that item in your garage")
#     else:
#         # otherwise, it does exist and we can delete it
#         del garage[item]

# def view_garage(garage):
#     # looping through the key, value pairs in our dictionary
#     for item, price in garage.items():
#         # printing out each item with its price set in the add_item function
#         print(f"{item}: ${price}")
#         # call the calculate_total function to add all the values (prices) in our dictionary
#     total = calculate_total(garage)
#     print(f"Your current garage total: ${total}")
    

# def calculate_total(garage):
#     prices = garage.values()
#     total = sum(prices)
#     return total



# def main(garage):
#     while True:
#         response = input("What would you like to do? 1. add 2. remove 3. view 4. quit and view total? ")

#         if response == "1":
#             add_item(garage)
#         elif response == "2":
#             remove_item(garage)
#         elif response == "3":
#             view_garage(garage)
#         elif response == "4":
#             print("Here is your total: ")
#             print(f" - ${calculate_total(garage)}")
#         else:
#             print("Please enter a valid response!")
# main(shopping_garage)

# Create an empty dictionary representing a garage
# key - item, value - location
# write functions to add, remove, and view your items in the garage
# create driver code to ask the user what they would like to do within the garage
# BONUS POINTS for updating item locations in the garge

garage_inv = {}

def add_item(garage):
    try:
        item = input("What would you like to add to the garage?")
        location = input("Where is it located?")
        quantity = int(input("How many of this item do you have"))
    except ValueError:
        print("Please input a number") 
    garage[item] = [location , quantity]


def remove_item(garage):
    item = input("Which item would you like to remove?")
    if item not in garage:
        print("That item is not in your garage")
    else:
        del garage[item]

def view_garage(garage):
    print(garage)
        # looping through the key, value pairs in our dictionary
    for item, info in garage.items():
        print(f"The {item}is located in {info[0]} and have {info[1]}")
        # printing out each item with its price set in the add_item function
        # for location, quantity in info:
            # print(f"The {item}is located in {location} and have {quantity}")
        # call the calculate_total function to add all the values (prices) in our dictionary

def main(garage):
    while True:
        response = input("""What would you like to do? 
                         1. add 
                         2. remove 
                         3. quantity 
                         4. quit and garage """)

        if response == "1":
            add_item(garage)
        elif response == "2":
            remove_item(garage)
        elif response == "3":
            view_garage(garage)
        elif response == "4":
            pass

        else:
            print("Please enter a valid response!")

 
main(garage_inv)