# a dictionary is an ordered collection of key value pairs

# decalring an empty dictionary - {}
kitchen = {}

print(kitchen)
print(type(kitchen))

 # adding key value pairs to the dictionary
kitchen = {
         #key   :  value
        "Spoons": "Top Drawer",
        "Plates": "Middle Shelf",
        "Cups": "Bottom Shelf"
 }

print(kitchen)
# keys in a dictionary are unique
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf",
    "Spoons": "Bottom Drawer" #reassigning the value of the key last one overwrites the first one
 }
print(kitchen)
# what can we use as keys in a dictionary?
#immutables types
int_dict = {
    1: "first key",
    2: "second key",
    3: "third key",
    3.4: "3.4th key"
}
print(int_dict)

# Accessing values in a dictionary
# dictionary_name[key]
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
#                  dict_name[key]
spoon_location = kitchen["Spoons"] #this gives us the value of Top Drawer
print(spoon_location)
print(kitchen["Plates"])

# be careful with using integers as keys becasue it makes it difficult
# to distinguish between dictionaries and lists
integers = {
    1: "first key",
    2: "second key",
    3: "third key",
    3.4: "3.4th key"
}
print(integers[1])

# using number strings as keys 
integers = {
    "1": "first key",
    "2": "second key",
    "3": "third key",
    "3.4": "3.4th key"
}
print(integers["2"])

# dictionaries introduce anew error KeyError
#keyError: 'key_name' if the key does not exist in the dictionary

kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
# print(kitchen["Forks"]) #KeyError: 'Forks'

# dict.get() <- return a value from a ky in our dictionary
# with no second argument, .get() will return none if the key isn't found
potential_item = kitchen.get("Blender")
print(potential_item)
# returnign the value of a found key
print(kitchen.get("Cups", "you dont have that item")) # Top Shelf
# only returns the second argument, if the key is not found ^
# .get() with a second argument
print(kitchen.get("Toast", "You don't have that item in your kitchen"))

# Adding and Updating our dictionary
community_center = {
    "Smash Tournament": "7 pm",
    "Yoga": "5 am"
}

# Adding to a dictionary
# dict[key to be added] = value to add at that key
# adding knitting to the dictionary
community_center["Knitting"] = "9 am"
print(community_center)
community_center["Zumba Session"] = "8 am"
print(community_center)
community_center["Art Gallery"] = "8 pm"
print(community_center)

# what if they key already exists?
# it updates the key to the new value
# updating a key, value pair
community_center["Yoga"] = "6 am"
# if they key already exits in the dictionary, it will set the key to the new value
print(community_center)

# creating a counter dictionary
counter_dict = {}
pokemon_cards = ["Charmander", "Blissey", "Jynx", "Jynx", "Jynx", "Milotic", "Milotic", "Blissey", "Charmander", "Jynx"]
for card in pokemon_cards:
    # if the card is in the dictionary already
    # then we've added it and need to increment the number of occurrences by 1
    if card in counter_dict:
        # counter_dict[cartd] = counter_dict[card] + 1
        counter_dict[card] += 1
    # first occurence of the card we set the value to one
    else:
        counter_dict[card] = 1
print(counter_dict)

# removing things from a dictionary
# dict.pop(thing_to_be_removed, value_if_not_found)
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
removed_item = inventory.pop("Apples") # return the value of the popped key
print(removed_item) # 30
print(inventory)
# popping a key that doesn't exist
# attempted_removal = inventory.pop("Canteloupe") # KeyError becuase Canteloupe is not in the dictionary
# popping a key that doesn't exist BUT giving pop a second argument
removed_value = inventory.pop("Canteloupe", "That doesn't exist to be removed")
print(removed_value)

# dict.popitem() -> remove and returns the last key, value pair added to the dictionary
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
inventory["Canteloupe"] = 25
print(inventory)
last_item_removed = inventory.popitem()
print(last_item_removed)
print(inventory)

# as of python 3.7 dictionaries are ordered

# del dict["key"] -> removes a key value pair from a dictionary doesnt return anything
# del entire key, value pair from a dictionary
# will give keyError if the key is not found
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
del inventory["Oranges"]
print(inventory)

# dict_.clear() -> clears all items in a dictionary
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
inventory.clear()
print(inventory)


# dict.keys() -> list of all the keys in a dictionary
contact = {
    "name": "Alice", "age": 30, "email": "alice@gmail.com"
}
print(contact.keys())
for key in contact.keys():
    print(key)

# looping through keys and using them to acces the value's
print("Here is your contact information: ")
for key in contact.keys():
    #      each key , value
    print(contact[key])

# by default looping through a dictionary acesses the keys
for info in contact:
    print(f"{info}: {contact[info]}") # output: name: Alice, age: 30, email:

# dict.values() -> list all of the values in a dictionary
temps = {"Monday": 97, "Tuesday": 92, "Wednesday": 94}
print(temps.values())
print("Here is the forecast for the next 3 days")
for temp in temps.values():
    print(temp)

# dict.items() -> returns a list of tuples with key in the first position and value in the second
# this is useful for looping through both the key and value
book_ratings = {"1984": 4.5, "Lord of the Rings": 5, "Brave New World": 4.3}

print(book_ratings.items())
for item in book_ratings.items():
    print(item) #refers to the key value pair (tuple)

for book, rating in book_ratings.items():
    print(f"{book} is rated {rating} stars")
    
# using sorted on a dictionaries keys or values
colors = {"red": 2, "blue": 5, "green": 1}
print(sorted(colors)) 
# sorts just the keys
print(sorted(colors.keys()))
# sorting the values
print(sorted(colors.values()))
# sorting the items
print(sorted(colors.items()))

# dict.updated({"key": "value"})  updates a dictionary with another dictionary
kitchen = {
    # key   :   value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}
# updating a current key - if the key already exists, we update it
kitchen.update({"Cups": "Middle Shelf"})
print(kitchen)
# if the key doesn't exist, we can add it
kitchen.update({"Air Fryer": "Counter Top"})
print(kitchen)
# updating a dictionary with more than one key value <- sets apart from the regular assignment
counter_top_stuff = {
    "Toaster": "Counter Top",
    "Cutting Board": "Counter Top",
    "Rice Cooker": "Counter Top",
    "Flowers": "Counter Top"                      
}
kitchen.update(counter_top_stuff)
print(kitchen)

# dict.setdefault(key, value) -> if the key is in the dictionary, return the value
inventory = {"apples": 30, "oranges": 40}
bananas = inventory.setdefault("bananas", 0)
print(bananas)
print(inventory)
apples = inventory.setdefault("apples")
print(apples)
print(inventory)
# with no second argument - add the key to the dictionary with a value of None
inventory.setdefault("canteloupe")
print(inventory)
# print(inventory[1:2]) TypeError cant slice a dictionary

# Create a dictionary with at least 2 key value pairs in it to start
# elaborate on the kitchen example or create your own collection
# add two new items with assignment dict[key] = value
# use .update to add at least 3 new items to your dictionary
# delete as many items as youd like using either pop or del


blakes_dict = {
    'name': 'Blake',
    'age': 19
}
blakes_dict['height'] = '6ft'   
blakes_dict['weight'] = '178lbs'
blakes_dict.update({'hair': 'brown', 'eyes': 'blue', 'knuckles': 'unpopped'})
blakes_dict.pop('knuckles')
print(blakes_dict)
# print(blakes_dict["Height"]) KeyError because of case sensitivity 
# blakes_dict["Height"] = "6ft 1" this adds a whole new item to the dictionary
# print(blakes_dict)


# NESTING COLLECTIONS IN DICTIONARIES
# NESTING COLLECTIONS IN DICTIONARIES
library = {
    "Fantasy": ["Harry Potter", "The Hobbit"],
    "Science Fiction": ["Dune", "Star Wars: Annihilation"],
    "Mystery": ["Sherlock Holmes", "And Then There Were None"]
}

# accessing a list that is as value in a dictionary
fantasy_books = library["Fantasy"]
print(fantasy_books)
for book in fantasy_books:
    print(book)

for book in library["Science Fiction"]:
    print(book)

# indexing into a list in a dictionary
print(library["Mystery"][1])
# ^ indexing into a list that is a value, using the key to get to the value
print(library["Fantasy"][2])

# adding an item to a list in a dictionary
library["Science Fiction"].append("The Martian")
print(library)


# looping through a dictionaries items and then the contents of its values - if they're lists

for genre, books in library.items():
    print(f"Here are the books for the {genre} genre: ")
    for book in books:
        print(f" - {book}")

# Dictionaries in lists
art_gallery = [
    {"Title": "Starry Night", "Artist": "Van Gogh", "Year": 1889},
    {"Title": "The Scream", "Artist": "Munch", "Year": 1893},
    {"Title": "Guernica", "Artist":"Picasso", "Year": 1937}
]
print(art_gallery)
# appending another dictionary to the list
art_gallery.append({"Title": "The Persistence of Memory", "Artist": "Dali", "Year": 1931})

print(art_gallery)

# looping through a list of dictionaries
for artwork in art_gallery:
    print(artwork["Title"], artwork["Artist"], artwork["Year"])

# looping through the list with dict.items()
for artwork in art_gallery:
    for info, value in artwork.items():
        print(f"{info}: {value}")

# Dictionaries in Dictionaries
museum_exhibits = {
    # each key represent a museum exhibit
    "Ancient Egypt":{"Artifacts": ["Sphinx", "Pyramids"],
        "Famous Pharoahs": ["Tutankhamun", "Cleopatra"]
    },
    "Renaissance Art": {
        "Notable Artists": ["Leonardo", "Michelangelo", "Rafael", "Donatello"],
        "Key Works": ["Mona Lisa", "The Last Supper"]
    }
}

print(museum_exhibits)
# adding a new key, value pair to a nested dictionary
museum_exhibits["Ancient Egypt"]["Recent Discoveries"] = ["New Tomb", "Ancient Slabs"]
print()
print(museum_exhibits)
museum_exhibits["Ancient Egypt"]["Famous Pharoahs"].append("Atem")
print(museum_exhibits)

# looping through ALL the items
for exhibit, details in museum_exhibits.items():
    print(f"Exhibit: {exhibit}")
    for section, items in details.items():
        print(f" - section {section}")
        for artifact in items:
            print(f"    -   {artifact}")


# #
# #service_tickets = {
#     "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}




