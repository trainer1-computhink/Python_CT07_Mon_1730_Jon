# # print("Hello from lesson 6")

# # pokemons = [
# #     "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
# #     "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
# #     "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
# #     "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
# #     "Electabuzz"
# # ]

# # powers = [
# #     55, 84, 49, 48, 45,
# #     45, 52, 55, 110, 110,
# #     85, 65, 134, 130, 110,
# #     50, 125, 65, 110, 83
# # ]

# # poke_power_list = []
# # poke_power = []

# # for i in range(len(powers)):
# #     poke_power_list.append([pokemons[i],powers[i]])

# # print(poke_power_list)

# # how are we going to retrieve all the pokemon name ?

# # for poke_power in poke_power_list:
# #     print(poke_power[0])

# bookshelf =[
#     ["water bottle", "kettle"],
#     ["note book", "textbook"],
#     ["home work", "personal work"]
# ]
# for shelf in bookshelf:
#     # print(shelf)
#     for item in shelf:
#         print(item)

# # Sample Code (Copy + Paste the below code):
# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# # ### the above is a nested list. Study and discuss it before we
# # ### move on.

# # 1. Write a for loop to print out the names of each student and
# #    the gender beside.
   
# #    e.g. Olivia F
# #         Noah M

# for student in students:
#     name, gender = student
#     print(name + " " + gender)

# names = ["Amy", "Ben", "Cal"]
# print(names[-2])

# grid = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]


# print(grid[1])
# result = grid[1]
# # result = [4, 5, 6]
# print(grid[1][2])
# board = [
#     [0, 1],
#     [2, 3]
# ]
# x = board[0][1]
# print(x)

arr = [1, 2, 3, 4, 5]
arr.pop()
arr.insert(2, arr.pop(0))
arr.append(arr.pop(3))
print(arr)
