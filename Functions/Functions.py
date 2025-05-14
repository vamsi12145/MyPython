#To avoid writing the same code multiple timeswe use function to call that particular code.
def calculate(exp):
    total=0
    for item in exp:
        total=total+item
    return total

list=[1000,2000,1200,3400]
list1=[2000,2400,1200]
expenses=calculate(list)
MonthlyExpenses=calculate(list1)
print(expenses,MonthlyExpenses)

#Positioned Arguments(7,9)
#Naming Arguments(a=7.b=9)
#Local and Global Variables
#the variables which is defined inside functions consider as local variables and which is defined outside as Global access
#__name__=__main__ this acts as a main function.


