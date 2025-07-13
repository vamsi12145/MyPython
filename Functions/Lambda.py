#Lambda is a annonymous function,In python Function can acts as objects
'''f=lambda a :a*a
result=f(5)
print(result)
'''
#Map is useful to transform the each element in a list
#Reduce is useful for aggregating all the elements in a list.
#Filter is used for filtering the list based on some conditions
#Above three functions are very useful in lambda functions
#Map Syntax -- map(function, iterables)
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)
#Filter
