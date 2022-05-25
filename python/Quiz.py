
# Quiz_6

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")


# Quiz_8

# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

# print("Day 1 - String Manipulation")
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")

# Quiz_10

# print(len(input("What is your name? ")))

# Quiz_12

# 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# c = a
# a = b
# b = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)


# Quiz_14

# print("Welcome to the Band Name Generator.")
# city = input("What's name of the city you grew up in?\n")
# name = input("What is your name?\n")

# print("hello " + name + "." + " I'm from " + city + ".")

# Quiz_19

# number = input()
# first_num = number[0]
# second_num = number[1]
# result = int(first_num) + int(second_num)
# print(result)


# Quiz_21

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = int(weight) / (float(height)** 2)
# print(round(bmi))


# Quiz_23

# age = input("What is your current age? ")

# days = (90 * 365) - (int(age) * 365)
# weeks = (90 * 52) - (int(age) * 52)
# months = (90 * 12) - (int(age) * 12)

# print(f"You have {days} days, {weeks} weeks and {months} months left")


# Project_24 - Tip Calculator

# print("Welcome to the tip calculator")
# bill = input("What was the total bill?  ")
# percent = input("What percentage tip would you like to give? 10, 12, or 15?  ")
# people_count = input("How many people to split the bill?  ")

# result = float(bill) * ((float(percent) / 100) + 1)
# result_percent = round(result, 2)
# pay =  round(result_percent / int(people_count), 2)
# pay = "{:.2f}".format(pay)

# print(f"Each person should pay: ${pay}")