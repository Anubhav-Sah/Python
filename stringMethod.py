#string are immutable

a="Anubhav"

a=a.upper()
print(a) 


#to strip we have to use rstrip() method

# for example

b= "Hello !!!! hello"

print(b.rstrip("!"))

#It will only remove last character from the string
#If you want to remove all characters from the string then you have to use lstrip() and


#replace() is used to replace the character in the string

# for example

print(b.replace("Hello","Hiii"))


#split(" ") is used to split the string into list

print(b.split(" "))




#capitalize() method turns only the first character of the string into uppercase and rest of the charecter into lower case

blogHeading ="introduction to python"
print(blogHeading.capitalize())


#center() method is used to center the string in the given width

str1="Welcome to my youtube channel"

print(str1.center(100))