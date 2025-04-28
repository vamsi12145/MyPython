'''import keyword

list=keyword.kwlist
print(list)'''
#This file is to write a list of Different operators that we use in the programming languages.
# Arithmetic Operators
#Comparison Operators
#Assignment Operators
#Logical Operators And ,Or, Not
#Bitwise Operators
#Membership Operators In,Not In
#Identity Operators   Is,Is not

#1.Arithmetic Operators

'''a=int(input("Give a random Number:"))# this is the way we do type casting in Python
b=int(input("Give a second Random Number:"))

print("For a=",a,"For b=",b,"\n Calculate the Following")

print("Addition of Two numbers:",a+b)
print("Multiplication of Two Number:",a*b)
print("Divisonof two numbers:",a/b)
print("Subtraction of two numbers:",a-b)
print("Floor Divison of Two numers:" ,a//b)
print("Reminder of two numbers:",a%b)
print("Exponent of Two Numbers:",a**b)

'''
'''
#2. Comparison Operators

a=77
b=98

print ("Two numbers are equal or not:",a==b)
print ("Two numbers are not equal or not:",a!=b)
print("a is less than b",a<=b)
print("a is greater than b:",a>=b)
print("a is less than b:",a<b)python
print("a is greater than b:",a>b)
'''
#Identity Operators

a=4
b=6

if(a is b):
  print("Both are equal")
else:
  print("Both are not Equal")

if(a is not b):
  print("Both are notequal")
else:
  print("Both are Equal")