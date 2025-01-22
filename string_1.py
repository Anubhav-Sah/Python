#what is String?

# In python,anything tht you enclose between single and double quotes is a string..
# String is a collection of characters.
# A string is essentially a sequence of array of textual data 
# String are used when working with Unicode characters


name = "Anubhav"
middleName = "Kumar"
surname ='Sah'

print("My name is " + name + " " + middleName + " " + surname)

#How to make a multiple line string in python?

multiLineString = '''Hello my name is Anubhav
I am a python developer
I am from India'''
print(multiLineString)


# Accessing Characters of a String 
# In python, string is like an array of characters. WE can access parts of string by using index. Index starts from 0.
# If you want to access the last character of a string, you can use -1 as index
name = "Anubhav"
print(name[0]) # prints A
print(name[-1]) # prints V
# Accessing multiple characters of a string
print(name[0:3]) # prints Anu
# Accessing multiple characters of a string from the end
print(name[-3:]) # prints hav

print("Printing the character of the string using for loop\n")

for character in multiLineString:
    print(character)


names ="Anubhav"


print(len(names))# use to count length

print(name[::-1])


nm ="Harry"
print(nm[-4:-2])

