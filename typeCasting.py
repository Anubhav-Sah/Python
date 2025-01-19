#***************************Typecasting***************************

#The conversion of a value from one data type to another is called typecasting.

#Python supports a wide variety of function or method like: int(),float(),ord(),hex(),oct(),tuple(),set(),list(),dict() etc. for the type casting in python.

#-------------------Type of Typecasting-------------------

#Explicit conversion : This is a type of typecasting where the programmer explicitly converts a value from one data type to another using a function or method.

a="2"
b="2"
print(a+b) #22
print(int(a)+int(b)) #4  here we have typecaster the value of a and b explicitly

#Implicit conversion : This is a type of typecasting where the python interpreter automatically converts a value from one data type to another without any explicit function or method.

a= 3.5
b= 4
print(a+b) #7.5  here python have typecasted b into float implicity
print(int(a)+b) #7 here we have explicity typecasted a from float to int

