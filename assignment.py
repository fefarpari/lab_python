#print message
x="Hello World"
print(x)

#add two numbers
x=10
y=10
print(x+y)

#odd and even     
number = int(input("Enter a number: "))
if number % 2 == 0:
  print(f"The number {number} is even.") 
else:
  print(f"The number {number} is odd.")
  
  
#leap year
year = int(input("Enter a year: "))
if (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
#print pi value    
import math
print("The value of pi is:", math.pi)

# store and print constant value
GRAVITY = 9.8
print("The constant value for gravity is:", GRAVITY) 

#square of a number
num = float(input("Enter a number: "))
square = num ** 2  
print("The square of", num, "is:", square)

#area of circle
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is: {area:.2f}")

#check datatype
my_variable = 10
if isinstance(my_variable, int):
    print(f"{my_variable} is an integer.")
    
#use math funcation

x = math.sqrt(64)
print(x)

# find power
result = pow(2, 3) 
print(result)

#check positive or negative
# The number to check
number = 5
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")



