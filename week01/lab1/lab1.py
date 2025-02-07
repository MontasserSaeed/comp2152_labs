#Sample Coding Questions 01 Week 01
#Pratik -FirstName
#Pokhrel -LastName
#Define an array variable with the following elements 1, 4, 7, 9
array = [1, 4, 7, 9]
#order of operations
a = 1
b = 2
c = 3
d = 4
#Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = (a - ((b**c) // d) + (a % c))
#Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

#common function
userAge = input('Enter your age: ')
userAge = int(userAge) + 22
print(f'Now showing the shop items filtered by your age: {userAge}')