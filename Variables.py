a=23
print(a,"->",type(a))

#In Python we don't need to give the data types explicitly it will take during runtime.

a=46
print(a)

a="Thank You Vamsi For showing up today"
print(a)
# Here Python is a  variables are dynamically typed so we can reassign values for the same variable.

# assigning same value to multiple variables  
var_1 = var_2 = var_3 = 182  

# assigning different values to multiple variables  
var_1, var_2, var_3 = 182, 'Tpointtech', '19.5'  


# implicit type casting  
var_2 = var_1 / 4  
print(var_2)  # int -> float  
  
# explicit type casting  
var_2 = int(var_2)  
print(var_2)  # float -> int  

#Scope of a variable

#del 
del var_1