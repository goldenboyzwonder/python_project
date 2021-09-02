#this logic uses a varible
message = 'hello world, this is my first python code'
print (message)

#this logic prints the message
print ('hello world!')

#using variables
firstText = "I love apples"
print(firstText)

#using variables that change
firstText = "I love apples"
print(firstText)
firstText = "I love bananas"
print(firstText)

#String Methods
string = "my name"
print(string.capitalize())
print(string.center(14))
print(string.title())
print(string.upper())

#f-string or format string
fName = "david"
lName = "blaine"
fulName = f"{fName} {lName}"
print(fulName.title())

animal1 = "bird"
animal2 = "man"
hero = f"{animal1} {animal2}"
print(hero)

fName = "Micheal"
lName = "Jordan"
fulName = f"{fName} {lName}"
print(f"Hello, my name is {fulName.lower()}!")

animal1 = "bat"
#did not add the variable animal2 because the variable did not change and is already declared
fulName = f"{animal1}{animal2}"
message = f"The name is {fulName.upper()}"
print(message)