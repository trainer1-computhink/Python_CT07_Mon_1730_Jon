# print("Hello from lesson 4")

# # ## Task 1: List of planets
# # **Task: Create a list of 8 planets in the solar system**

# # **Task 1a**:
# # Create a list of 8 planets in the solar system.
# # (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# # planets.insert(3, "Mars 1.0")
# planets.append("Pluto")
# planets.insert(20, "Pluto 1.0")
# print(planets)
# del(planets[7])
# print(planets)
# planets.pop(7)
# print(planets)
# # planets.pop(1)
# # print(planets)
# popped_planet = planets.pop(7)
# print(popped_planet)

# for planet in planets:
#     # print(planet)

#     if planet == "Earth":
#         print(planet + ": this is my home")

#     elif planet == "Mars":
#         print(planet + ": I conquered it")
#     else:
#         print(planet)




# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list

# ---------------------------------------------------------------

# ## Task 2: List of planets (part 2)
# Tasks:

# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or changed name), print
#    "<planet name> : I conquered this"
# 4. If name == "Lalaland", print
#    "<planet name> : I created this"

# ---------------------------------------------------------------

# ## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ... 

# ---------------------------------------------------------------

# ## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# menu_list = []
# manager_input = input("What is the food items? (type end to stop input): ")
# while manager_input != "end":
#     menu_list.append(manager_input)
#     manager_input = input("What is the food items? (type end to stop input): ")
# print(f"The menu items is {menu_list}")

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."
