print("Hello world")


#if you want to make a multi-line comment then we hava to use triple quotes


'''
hello world 
this is a multi line comment

'''



#******************Escape Sequences*******************

# Escape Sequence	Description	Example	Output
# \'	Single quote	print('It\'s Python!')	It's Python!
# \"	Double quote	print("He said \"Hi\"")	He said "Hi"
# \\	Backslash	print("C:\\path\\to\\file")	C:\path\to\file
# \n	Newline	print("Hello\nWorld")	Hello 
#                                       World
# \t	Tab	print("Hello\tWorld")	Hello   World
# \r	Carriage return (moves the cursor to the beginning of the line)	print("Hello\rWorld")	World
# \b	Backspace	print("Hello\bWorld")	HellWorld
# \f	Form feed (new page)	print("Hello\fWorld")	Hello World (page break)
# \v	Vertical tab	print("Hello\vWorld")	Hello World (vertically)
# \a	ASCII Bell (makes a beep sound)	print("\a")	Beep sound
# \N{name}	Unicode character by name	print("\N{degree sign}")	°
# \uXXXX	Unicode character with 16-bit hex value	print("\u00B0")	°
# \UXXXXXXXX	Unicode character with 32-bit hex value	print("\U0001F600")	😀
# \xhh	Character with hexadecimal value	print("\x41")	A
#we can add nultiple escape sequences in a single string



#we can sapareate the value in print function using comma


print("Hello", "World", "Python")

print("Anubhav","M",19)

#Seperator in print function
#seperator is used to separete the value in print function

print("Anubhav","M",19, sep=("-"))


# end in print function
#end is used to add a string at the end of the print function
print("Hello ", end= "")
print("World")#this will not print anything
