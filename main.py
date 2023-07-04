# print("Hello World\n")

# print(5+8)

# Indetation
# if(age<18):
#     print("hello")

# comments
# single line cmt
''' 
Multi Line cmnt
'''

# Modules and Import statement
# import (Package name)
# ex import math
# import math

# print(math.gcd(3,6))

# Variables 
# 1. variables should start with a letter or _
# 2. variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensetive eg: a and A are two different variables
# a = 10
# b = "Prateek"
# c = 10.54
# is_adult = True

# print(a)
# print(a+5)
# print(a+c)
# we can chage value by reassign value
# a =15

# type of variable
# typea = type(a)
# print(typea)

# Type-Casting :
# Type-casting is defined as converting one data type into another for smooth functioning of program.
# e = "50" 
# print(type(e))
# e = int(50)
# print(e+2)

# test
# a = 15
# b = "25"
# print(type(b))
# b = int(b)
# print(type(b) )
# print("Sum of a and b is",a+b)

# Input fn
# This function takes the input from user but it always take input in string data type i.e. if we want any arithmetic operation to be done on that input then we need to type cast that input into either int or float data type.
# name = input("What is your name? ")
# we give input and its in string

# another example

# a = int(input("Enter any number: "))  # here we use int before input function so that when we give input it convert it into integer
# name = int(input("Enter any name: "))
# print(type(a))
# print(a)
# print(type(name))
# print(name)

# concatenation
# print("Hello" +" " + name)

# String
# String literal in python are enclosed in either single quotes (‘’) or double quotes (“”).
# It means “hello” is same as ‘hello’.
# We can simply assign string to a variable.
# print("\t\t Strings")
# a = "Hello"
# print(a)

# demo = '''
# This is an
# example of
# multi-line
# string.
# '''
# print((demo))

# here we declared a variable Demo and in that variable we assigned a multi-line string.
# In multi-line strings also we can use either single quotation mark or double quotation mark.


# String Slicing :
# In Python to use any specific character of string we use index no.
# Index no. is a special type of no. which allows us to extract any character from string.
# Index no. starts from 0.
# a = "Hello"
# print(a[0])
# print(a[1])
# print(a[2:5])

# String Functions :
# variable_name.strip() = This function allows us to remove all the blank spaces near to string.
# a = "   Hello  "
# print(a)
# print(a.strip())

# len() = len function counts the total characters of any string.
# a = "Hello"
# print(a)
# print(len(a))

# variable_name.lower() = This function converts all the characters in lower case of a string.
# a = "Hello"

# print(a)
# print("\n")
# print(a.lower())

# variable_name.upper() = This function converts all the characters in upper case of a string.
# a = "Hello"

# print(a)
# print("\n")
# print(a.upper())

# variable_name.replace(“char1”, ”char2”) = This function replaces char1 by char2 in a string.

# a = "Hello"
# print(a)
# print(a.replace('ello', 'i'))

# Adding Strings :
# We can simply add two or more strings by using ‘+’ operator between two variables.
# a = "Hello"
# b = " Guys"
# print(a+b)

# Format Strings :
# It means we can easily format string by using .format function.
# a = "Demo"
# b = "Format"
# print("This is the {} string".format(a,b))
# print("This is the {0} string".format(a,b))
# print("This is the {1} string".format(a,b))

# In placeholders we can pass values such as 0,1 etc.
# a = "Demo"
# b = "Format"
# in python3 introduced f(string)
# print(f"This is a {a} of {b} string")

# operators
# a = 10
# b = 20

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# try these 
# ** Exponentional (power)
# // floor division (return a integer)
# % modulo (remainder)

# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print( 5 // 2)
# print(5 % 2)
# print(5 ** 2)

# Python Data Collections:
# In Python there are some built-in or core data types :

# Lists
# Tuples
# Sets
# Dictionaries
# Let's discuss each of them in brief.

# Lists
# A List in Python represents a list of comma-separated values of any data type between square brackets.
# lst = [51,2,3,4,5,10,20]
# print(lst)
# print(type(lst))
# print(lst[0])
# print(lst[1])
# print(lst[2: 5])      # (x:y mean start from 2 till 5)

# List Functions :
# variable_name(list).append – This function adds a new value or element in the end of the list.

# lst.append(99)      #append runction
# print(lst)

# variable_name(list).insert(index_no, value) – This function adds a new element at any index no. in the list.

# lst.insert(0,99)        #insert runction
# print(lst)

# variable(list).remove(element) – This function removes an element from the list.

# lst.remove(2)       #remove runction
# print(lst)

# variable(list).pop() – This function removes one element from the end of the list.

# lst.pop()       #remove one element from list
# print(lst)

# del variable[index_no] – This keywords allows us to remove or delete any particular element from the list by using it’s index no.

# del lst[2]       #remove the element at index 2
# print(lst)

# del variable(list) – This is used to delete whole list from the program.
# del lst
# Variable(list).clear – This function removes all the elements of the list.

# lst.clear()       #clears the list
# print(lst)

# *Don't get bother about all the methods just google it and learn whatever is imp for you


# Tuples:
# These are those lists which cannot be changed i.e., are not modifiable. Tuples are represented as list of comma-separated values of any date type within parentheses.
# Tuples doesn’t allow modification.

# If we wish to modify any tuple then we’ll get error but we can modify type after converting or type casting it into the list.

# tup = ('Demo', 'Hello', 54, 'Guys')
# print(tup)
# print(type(tup))
# tup[1] = 99 #cannot do this
# tup = list(tup)
# * as we know we can't edit tuple so, if we want to edit tuple convert it into list and then edit it
# tup[1] = 99
# print(tup)

# *Most of methods of list yoy can use  and yes go and search for tuple function and use it as you want

# Sets :
# We all already studied in 10th and 12th i.e set is a collection of well defined objects
# here same like that

# Sets in python are a data type equivalent to sets in mathematics. It may consist various elements and the order is undefined.

# Sets elements are enclosed in {} Curly Braces.

# In sets repeated elements does not get printed.

# s1 = {2,2,2,2,3,4,5,6,6,6,7,8,9,0,23,56,76,23}
# print(s1)

# here we can do add, update and alot

# Sets Functions :
# variable_name.add(element ) – This function is used to add one element in the Set.
# s1.add(99)
# print(s1)

# variable_name.update([element1, 2, 3…]) – This function allows us to add many elements in the set.
# s1.update([5,6,99,199])
# print(s1)
# *we use update when we need to add more than one number
# There are many more functions of sets such as .pop, .clear, del etc. Try them in your computer.

# Dictionary :
# Dictionary data type is another feature in Python's hat. The dictionary is an unordered set of comma-separated key: value pairs, within {},with the requirement that within a dictionary, no two keys can be the same (i.e., there are unique keys within a dictionary).

# dictionary1 = {
#     "Play" : "Doing some activity",
#     "Food" : "Something eatable",
#     "Python" : "Language",
# }

# print(dictionary1)
# print(len(dictionary1))

# *Dictionary Functions are same as of list, tuples etc. 

# Conditional Statements :
# These are complex statements which possess some conditions. It means in these statements control only enters when the condition is true.

# In conditional statements we have 3 type of statements :

# if statement
# if-else statement
# elif statement


# if statement – In if statement condition is checked and if the condition is true then body of if statement get executed.

# x = int(input("Enter any number: "))
# if (x>100):
#     print("Number entered is greater than 100")

# print("END!")

# if-else statement – In if-else statements condition is checked and if condition is true then block of if statement get executed but if ‘if’ condition is false then block of else statement get executed.

# age = int(input("Enter your age: "))

# if (age>18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# elif statement – In these type of statements, there are many instances when there is a need to check condition. We use these statements when we have to check many conditions.

# It simply means we are checking each statements and when we find match it executed

# x = int(input("Enter any number: ")

# if (x>50):
#     print("Number is greater than 50")
# elif (x>25):
#     print("No. entered is b/w 25-50")
# elif (x>0):
#     print("Number entered is between 0-25")
# else:
#     print("Enter valid number")


# Loops :
# Imagine you have to print number from 1 to 100
# for i in range(0,100):
#     print(i)



# Loops or iterative statements are the statements which allow repetition of block of code again and again till the condition become false.

# There are 2 type of loops in Python :

# for Loop and while loop.

# we can use for loop in list also:

# li = [3,9876, "Test", "Pass"]
# for item in li:
#     print(item)

#see it itrate all the items of loop

# write table of 5
# num = 5
# for a in range(1, 11 ):
#     print(num, 'x ', a, '=', num* a)




# While loop

# i = 1 
# while i <= 5:
#     print(i)
#     i= i+1

    # Explain: here we assign value to i and then use while loop and ask to print till value matches 5

    # Another example

#     x = 1
# while(x<=100):      #while loop
#     print(x)
#     x = x+1

# Functions :
# A function is a block of codes that take inputs, do some specific task and produces output. We create functions when we have to do some work again and again in a program. That’s why we create function and calls it whenever we want to use it in our program.

# in simple words, it is a block of code which we can run whenever we want by just calling its name

# Creating a function :

'''
def function_name () :

         statement 1,

         statement 2,

'''
# def funct() :
#     print("Hi There")

# funct()
# another example
# def demo():     #Defining a function
#     print("Hlo Guys")
#     print("It's my First Function")
#     print(" : )")

# demo()      # Calling a function

# lets create another function

# def sum(a,b):       #it takes any two values as argument
#            c = a+b
#            return c

# d = sum(50,100)    
# print(d)

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# z = sum(x,y)        #Calling Function
# print("The Sum is", z)

# OOP (Object Oriented Programming) :