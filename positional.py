#basic positional argument
def add (a,b):
    print("a =",a)
    print("b =",b)
    return a+b
result=add(2,5)
print("sum =",result)

#student information
def student_info (name,roll,marks):
    print("name : ",name)
    print("roll no : ",roll)
    print("marks : ",marks)
student_info("pari",24,100)

#simple interest
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest : ",si)
simple_interest(10000,2,3)
simple_interest(40000,1.2,3)

#area of circle
def ar_circle(r):
    a_circle=3.14*r*r
    print("area of circle : ",a_circle)
ar_circle(2.4)
ar_circle(10)

#check number positive negative or zero
def check_value(no):
    if(no>0):
       print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(-167)
check_value(40)

#odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
odd_even(60)
odd_even(31)

#arithmetic operation subtraction,muitiplication,division
def addition (a,b):
    add= a+b
    print("addition of two values",add)
addition(34,25)
addition(24,29)

