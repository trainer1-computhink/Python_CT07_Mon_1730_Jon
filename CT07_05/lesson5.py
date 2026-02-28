# print("Hello from lesson 5")


# import random
# lucky_num_list = []

# for _ in range(1000):
#     lucky_num_list.append(random.randint(1,1000))

# print(lucky_num_list)

# # for i in range(100):
# #     if i in lucky_num_list:
# #         print("True")
# #     else:
# #         print("False")

# print(lucky_num_list.index(1001))

## Task 5: Pokemon, I choose you!
# Task: You are given 2 lists,
# **pokemons** contains a list of pokemons
# **powers** contains a list of the corresponding pokemon's
#            powers

# 1. Choose 2 random pokemons from the list
# 2. Compare the powers of the 2 pokemons
# 3. Calculate who is the winner of the fight between these 2
#    pokemons
#    (pokemon with the higher power will always win)

# Sample data (Copy + paste the below code):
pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]


# Hint: import the random library and use random.choice(listname)
import random
poke1 = random.choice(pokemons)
poke2 = random.choice(pokemons)

# find out what is their power? 
# how?
# 1st, we need to know where is poke1 and poke2 at in the pokemons list
# so we need to find their index
# we use pokemons.index("name of the pokemon")
poke1_ind = pokemons.index(poke1)
poke2_ind = pokemons.index(poke2)

# now we find the index of poke1 and poke2, what is nexT?
# we can use the index to find out the power of poke1 and poke2 from the powers
poke1_power = powers[poke1_ind]
poke2_power = powers[poke2_ind]

# now that we know the power, we let them fight at who win
# win 
# lose
# tie

print(poke1 + " and " + poke2 + " is fighting.")
if poke1_power == poke2_power:
    print("It is a tie.")
elif poke1_power > poke2_power:
    print(poke1 + " wins.")
else:
    print(poke2 + " wins.")

