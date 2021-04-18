# import random

# # integer
# random_integer = random.randint(1, 100)
# print(random_integer)

# # float generates numberes between 0 and 1
# random_float = random.random()
# print(random_float)


# #float create a random decimal number between 0 and 5
# random_float_decimal = random.random() * 5
# print(random_float_decimal)



#List

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]# print(states_of_america[0])

# #store in a variable
# state = states_of_america[2]
# print(state)

#negative index, starts counting from the end of the list, because you can't have -0
print(states_of_america[-1])
# i get new jersey

#change things on the list
states_of_america[1] = 'Pencilbania'
print(states_of_america)

#add to the end of the list
states_of_america.append("Aneland")
print(states_of_america)

#extend add to the end of the list a bunch of new items
states_of_america.extend(["Coperland", "Pepelad"])
print(states_of_america)
