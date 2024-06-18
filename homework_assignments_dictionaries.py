# 1. Real-World Python Dictionary Applications

# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. 
# You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def main(restaurant_menu):
    # Add a new category called "Beverages" with at least two items.
    restaurant_menu["Beverages"] = {"Coke": 2.99, "Dr. Pepper": 2.99}
    print(restaurant_menu)
    # Update the price of "Steak" to 17.99.
    restaurant_menu["Main Course"]["Steak"] = 17.99
    print(restaurant_menu)
    # Remove "Bruschetta" from "Starters".
    del restaurant_menu["Starters"]["Bruschetta"]
    print(restaurant_menu)

# main(restaurant_menu)

# 2. Python Programming Challenges for Customer Service Data Handling

# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:


service_tickets = {
    "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(service_tickets): 
    input_customer = input("Please tell me you name your name: ") # get customer name
    input_issue = input("PLease enter the issue you are experiencing: ") # get issue
    ticket_number = "Ticket" + str(len(service_tickets) + 1) # take the current ticket number and add 1 to it
    service_tickets[ticket_number] = {"Customer": input_customer, "Issue": input_issue, "Status": "open"} # add the new ticket to the service_tickets dictionary
    print(f"{ticket_number} has been opened for {input_customer} with {input_issue} issue") # take all iputs provided and print them out let them know the ticket has been opened


def ticket_status(service_tickets):
    while True:
        user_input = input("What ticket do you need to change the staus of? Ticket#: ")
        user_input =  user_input.capitalize()
        if user_input in service_tickets: # check if the ticket exists
            try: # if the ticket exists ask the user to input the status they would like to change it to
                status_input = int(input("What is the current status of this ticket?: 1. open 2. closed "))
                if status_input == 1:
                    service_tickets[user_input]["Status"] = "open" #if they choose 1 it opens the dictionary looking for the user input ticket and changes the status to open
                    print(f"{user_input} in now set to open") # prompts that its now open
                    break # breaks the loop
                elif status_input == 2:
                        service_tickets[user_input]["Status"] = "closed" #if they choose 2 it opens the dictionary looking for the user input ticket and changes the status to closed
                        print(f"{user_input} in now set to closed")  # prompts that its now closed
                        break
                else:
                        print("Please enter a valid number") # if the user enters a number that is not 1 or 2 it prompts them to enter a valid number
            except ValueError:
                print("Please enter a valid number")   # if user enter something other then numbers prpmpts to enter a number
        else:
            print("Ticket does not exist") #if the user iputs anything other then ticket# it prompts that the ticket does not exist
            



def display_tickets(service_tickets): # display all tickets
        print("Here are all the tickets: ")
        for ticket, info in service_tickets.items(): #loop through the dictionary to set the key as a variable
            print(f"{ticket}:") #print the key variable (Ticket#)
            for key, value in info.items(): #loop through the dictionary to set the key and value as variables
                print(f"        {key}: {value}") #print out the info in the dictionary

def filter_tickets(service_tickets):
    user_input = input("What status would you like to filter by? 'open' or 'closed': ")
    for ticket, info in service_tickets.items():
        if info["Status"] == user_input: # same print out as above but only showe the tickets that = the user input
            print(f"{ticket}:")
            for key, value in info.items():
                print(f"        {key}: {value}")

def main(service_tickets):
    while True:
        print("""
            1. Open a new ticket
            2. Change ticket status
            3. Display all tickets
            4. Filter tickets by status    
            """)
        user_choice = input("Please tell me what you would like to do: ")
        
        if user_choice == "1": # if user chooses 1 it runs the open_ticket function
            open_ticket(service_tickets)
        elif user_choice == "2": # if user chooses 2 it runs the ticket_status function
            ticket_status(service_tickets)
        elif user_choice == "3":# if user chooses 3 it runs the display_tickets function
            display_tickets(service_tickets)
        elif user_choice == "4":# if user chooses 4 it runs the filter_tickets function
            filter_tickets(service_tickets)

main(service_tickets) #runs the main function
