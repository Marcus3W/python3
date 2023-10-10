dog_foods = {"Blue Buffalo": 5, "Purina": 7, "Iams": 3, "Pedigree": 2}

for food_brand in dog_foods:
    print(food_brand + " has " + str(dog_foods[food_brand]) + " bags")

# What is happening here?

# The for loop is iterating through the keys of the dictionary, and the print statement is 
# printing the key and the value of the key.

dog_foods_iterator = iter(dog_foods)

print(dog_foods_iterator)
# print(dir(dog_foods))

print(dog_foods.__iter__())