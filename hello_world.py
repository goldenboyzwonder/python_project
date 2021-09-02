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

fName, lName = "care", "bear"
msg = f"{fName} {lName}"
print(msg)

#numbers
print(2+4*3)

#number example (2)
x,y,z = 1,2,3
print(y,z)


#indicate a constant variable FNAME even though python doesn't do constants
#the all caps show that the variable is constant and shouldn't change
FNAME = "jerjer"
print(FNAME)

#creating a list
nameLst = ["hello", "jumping", "mike"]
print(nameLst[1].upper())

changing = f"all I am doing is {nameLst[1].upper()}!"
print(changing)

#create/modify list
strgList = ["yamaha", "suzuki", "harley-davidson"]
strgList[0] = "ducati"
print(strgList)

strgList.append("yamaha")
print(strgList)