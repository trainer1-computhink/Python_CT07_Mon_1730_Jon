# # Lesson 8 - Input Validation

# ## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

# ## Task 1: Data Format Check

# ### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.

# ### Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# ### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# ## Task 2: Length Check (using a while loop)

# ### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!

# ### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.
# while True:
#     user_name = input("What is the username?")
#     if user_name.isalnum() and len(user_name) >= 5 and len(user_name) <=18:
#         break
# print(user_name)


# ## Task 3: Range Check (using a while loop)

# ### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.
# while True:
#     birth_year = input("What is your birth year? ")
#     if birth_year.isdigit() and int(birth_year) >= 1900 and int(birth_year) <= 2026:
#         break
# print(birth_year)


# ### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.
# while True:
#     volume = input("What is the volume? ")
#     valid = True

#     if not volume.isdigit():
#         print("The volume should be digits")
#         continue

#     if not (int(volume) >0 and int(volume) <= 100):
#         print("the volume should be between 0 and 100")
#         continue

#     if valid:
#         break
# print(f"Volume is {volume}")

# word = "DraGonite"
# print(word.upper())
# print(word.lower())
# sentence = input("What is your sentences?")
# new_sentence = ""
# for i in range(len(sentence)):
#     if i % 2 == 0:
#         new_sentence += sentence[i].upper()
#     else:
#         new_sentence += sentence[i].lower()
# print(new_sentence)

# sentence = input("What is your sentence? ")
# new_sentence = ""
# is_upper = True
# for char in sentence:
#     if char.isalpha():
#         if is_upper:
#             new_sentence += char.upper()
#         else:
#             new_sentence += char.lower()
#         is_upper = not is_upper
#     else:
#         new_sentence += char
# print(new_sentence)


# ## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.
# word = "dragonite"
# print(word[3:5]) 
# word = "SINGAPORE"
# print(word[:4])
# word[4:6]
# word[6:10]
# word[:10:2]
# ## Task 5: Slice String
# word = “SINGAPORE”

# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE

# ## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.
# word = "charizard"
# # print(word[::-1])

# while True:
#     word = input("What is the word? ")
#     if word.lower() == "end":
#         break
#     if word == word[::-1]:
#         print(word + " is a palindrome")
#     else:
#         print(word + " is not palindrome")

# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

# ## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
friends = ["Alice", "Bob", "Carl", "Dylan"]

# while True: 
#     valid = True
#     name = input("What is your name?").strip()
#     if name == "": # Presence check
#         print("Please enter your name.")
#         valid = False

#     if valid:
#         break

# if name in friends: #existence check
#     print("Name is in the list, entry approved.")
# else:
#     print("Name is not in the list, entry denied.")
        


# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

# ## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

# ## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me
