# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ['Kiwi', 'Papaya', 'Fig', 'Pomegranate', 'Lime',]
# TODO: Add a fruit to the end of the list
fruits.append('Coconut')

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, 'apple')

fruits = ['Watermelon'] + fruits

# TODO: Remove a fruit from the list
fruits.remove('Fig')

# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
list = [1, 2, 3, 4, 5]
# TODO: Create a new list with each number squared

# option 1
squared = [x**2 for x in list]
print(squared)

# Option 2
squared = []  
for x in list:        
    squared.append(x**2)
    print(squared) 
# TODO: Find the sum and average of the original numbers
total = sum(list)
av= sum(list)/len(list)
# TODO: Print the results
print(f"The sum is: {total}")
print(f"The average is: {av}")

#-------------------------------------------------------------------------
# # Question 3: Creating and Modifying Dictionaries
 
# TODO: Create a dictionary of countries and their capitals
dictionary = {"namibia": "windhoek",
"angola": "luanda",
"morocco": "casablanca",
"bostwana": "gaborone",
"lesotho": "maseru"
}
# TODO: Add a new "sa":"pretoria"country-capital pair
dictionary.update({"sa":"pretoria"})

# TODO: Update the capital of an existing country
dictionary.update({"morocco":"rabat"})
# TODO: Remove a country-capital pair
del dictionary["angola"]
# dictionary.pop("angola")
# TODO: Print the modified dictionary
print(dictionary)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
colors = {"apple": "green",
"banana": "yellow",
"berry": "blue",
"strawberry": "red",
"avocado": "black",
}
# TODO: Print all the fruits (keys)

# option 1
for key in colors:
    print(key)

# Option 2
print(colors.keys())

# TODO: Print all the colors (values)

# Option 1
for values in colors.values():
    print(values)

# Option 2
print(colors.values())
# TODO: Print each fruit and its color

for fruit, color in colors.items():
    print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color

print("write the name of a fruit")
check = input("Colour: ")
if check in colors:
    print(f"The color of {check} is {colors[check]}.")
else:
    print(f"{check} is not in the dictionary.")
