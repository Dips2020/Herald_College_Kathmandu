# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -----------------------------------------------------------------------------------------------------
# From here
# 1. example
# def greet(name):
#     print("Hi,"+name+"!")
# greet("DiPS")

# 2. example
# def info(name, age, stud_id):
#     print("Your name:"+name, "Your age:"+age, "Student id:"+stud_id)
# info("Dipesh", "20", "123456")

# 3. example
# def val(x, y):
#     return x*y
#
#     # add=x+y
#     # sub= x-y
#     mul = x * y
#     # return mul,add,sub
#
# Multiply = val(2,3)
# print("Your ans:", Multiply)

# 4. example
# message = "Dipesh"
# def gl():
#     print("Name", message)
# gl()

# 5. example
# def greet(name):
#     '''Hello there'''
#     print(f"How are you, {name}!")
# print(greet.__doc__)
# greet(name="Dipesh")

# 6. example .___doc___
# def welcome():
#     """welcome to this program"""
# print(welcome.__doc__)

# first_name = "Dipesh"
# last_name = "Bhattarai"
#
# full_name = first_name+" "+last_name
# # full_name = last_name+" "+first_name
# reversed_name = full_name[:: -1]
# print(reversed_name)

# first_num = 2
# second_num = 3
#
# sum = first_num + second_num
# product  = first_num * second_num
#
# print(sum, product)

# # take user input for the number
# num = int(input("Enter a number: "))
#
# # calculate the remainder
# remainder = num % 2
#
# # print the remainder
# print("The remainder of", num, "when divided by 2 is", remainder)

# num = int(input("Enter a number: "))
# remainder = num % 2
#
# print("The remainder of", num, "when divided by 2 is", remainder)

# # take user input for weight in kilograms and height in centimeters
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in centimeters: "))
#
# # convert height to meters and calculate BMI
# height_m = height / 100  # convert height to meters
# bmi = weight / (height_m ** 2)  # calculate BMI
#
# # print the result
# print("Your BMI is:", bmi)
#
#
# import math
# # # Input radius of the hemisphere
# radius = float(input("Enter the radius of the hemisphere: "))
# # # Calculate the surface area of the hemisphere
# surface_area = 2 * math.pi * radius ** 2
# # Display the surface area of the hemisphere
# print("The total surface area of the hemisphere is:", surface_area)
# num = int(input("Enter a number: "))
# cube = num ** 1/3
# print("Cube of number: ", cube)
#
# temperature = float(input("Enter a temperature in Celsius: "))
# Fahrenheit = (temperature*9/5) + 32
# print(f'Temperature is: {Fahrenheit}')

# def leap_year(y):
#     if (y % 4 == 0):
#         print(f'It is a leap year {y}')
#     else:
#         print(f'not a leap year {y}')
#
# year = int(input("Enter the year: "))
# leap_year(year)
#
# def divisible(d):
#     if (d %2==0 and d % 3 ==0):
#         print(f'Is divisible by both 2 and 3: {d}')
#
#     else:
#         print(f'Not divisible by both 2 and 3: {d}')
# number = int(input('Enter the number: '))
# divisible(number)

#
# radius = float(input("Enter the radius: "))
# pi = 3.14
#
# Area = pi * radius**2
# print(f"The Area: {Area:.2f}")


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# address = input("Enter your address: ")
#
# details = "My name is %s. I am %d years old and I live at %s." % (name, age, address)
#
# print(details)


# cost_price = float(input("Enter the cost price of the gadget: "))
# vat = cost_price * 0.13
# # print("The VAT amount is: {:.2f}".format(vat))
# print(f"The VAT amount is: {vat:.2f}")


# =========================== ⬇️ Workshop 3 ⬇️ ===========================

# Part 2
# number = input("Enter a number: ")
# def types(x):
#     print("Value is integer: ",float(x))
#     print("Value is float: ",int(x))
# types(number)


# num = int(input("Enter a number: "))
# def squared(n):
#    print("The square of a number: ", n**2)
# squared(num)

# num = int(input("Enter a integer number: "))
# def number(n):
#     print(f"The type of {n} is {type(n)}")
#     turn = str(n)
#     print(f"The type of {n} is {type(turn)}")
# number(num)

#
# na_me = input("Enter your name: ")
# def hello_world(name):
#     print("Hello World, my name is: ", name)
#
# hello_world(na_me)


# def values(n,y):
#     divide = n/y
#     formatted = format(divide, '.2f')
#     print(formatted)
# first_num = int(input("Enter a 1st number: "))
# second_num = int(input("Enter a 2nd number: "))
# values(first_num, second_num)

# 2.	Create a Python program called calculator with functions to perform the following arithmetic calculations, each should take two parameters and return the result of the arithmetic calculation in question.
# A) Addition (+)
# B) Subtraction (-)
# C) Multiplication (*)
# D) Division (/)
# E) Modulus (%)
# F) Exponentiation (**)
#
# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# def modulus(x, y):
#     return x % y
#
# def exponentiation(x, y):
#     return x ** y
# x = int(input("Enter a 1st number: "))
# y = int(input("Enter a 2nd number: "))
# print(add(x, y), subtract(x, y), modulus(x, y), multiply(x, y), divide(x, y), exponentiation(x, y))
# print(add(4, 8))
# print(subtract(4, 8))
# print(multiply(4, 8))
# print(divide(4, 8))
# print(modulus(4, 8))
# print(exponentiation(4, 8))


# 3.	Go back and add multiline Docstrings to each of the functions you defined in the previous question. Use the help function to check them afterwards.3.	Go back and add multiline Docstrings to each of the functions you defined in the previous question. Use the help function to check them afterwards.
# def add(x, y):
#     '''this is .__doc__ addition '''
#     print(f"{x+y}")
#
# def subtract(x, y):
#     '''this is .__doc__ subtract '''
#     print(f"{x-y}")
#
# def multiply(x, y):
#     '''this is .__doc__ multiplication '''
#     print(f"{x*y}")
#
# def divide(x, y):
#     '''this is .__doc__ divide '''
#     print(f"{x/y}")
#
# def modulus(x, y):
#     ''' this is modulus'''
#     print(f"{x%y}")
#
# def exponentiation(x, y):
#     '''this is .__doc__ exponentiation '''
#     print(f"{x**y}")
# x = int(input("Enter a 1st number: "))
# y = int(input("Enter a 2nd number: "))
# # print(add(x, y), subtract(x, y), modulus(x, y), multiply(x, y), divide(x, y), exponentiation(x, y))
# print(add.__doc__)
# add(x, y)
# print(subtract.__doc__)
# subtract(x, y)
# print(multiply.__doc__)
# multiply(x, y)
# print(divide.__doc__)
# divide(x, y)
# print(modulus.__doc__)
# modulus(x, y)
# print(exponentiation.__doc__)
# exponentiation(x, y)

# 1.	A python function “avg” returns the average of three values, as shown below:
# def avg (num1, num2, num3):
# return (num1 + num2 + num3) / 3.0
# n1, n2, n3 = 37, 108, 67
# num1 = 37
# num2 = 108
# num3 = 67
# def avg(num1, num2, num3):
#     return(num1 + num2 + num3) / 3


# E. improved_average( ) that takes five integer parameters. It should return the mode, median and mean values of the numbers passed to the function.
# def improved_average(num1, num2, num3, num4, num5):
#     mean = (num1+num2+num3+num4+num5)/5
#     return mean
#
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))
# num5 = int(input("Enter 5th number: "))


#
# assignment_1 = float(input("Science Marks: "))
# assignment_2 = float(input("Computer Marks: "))
# assignment_3 = float(input("English Marks: "))
# assignment_4 = float(input("Mathematics Marks: "))
# assignment_5 = float(input("Optional Math Marks: "))
# total_score = (assignment_1+assignment_2+assignment_3+assignment_4+assignment_5)
# percentage = (total_score/500)*100
# avg = total_score/5
# if avg>=90:
#     grade = "A"
# elif avg>= 80 and avg<90:
#     grade = "B"
# elif avg>=70 and avg<80:
#     grade = "C+"
# elif avg>=60 and avg<70:
#     grade = "C"
# elif avg >=50 and avg<60:
#    grade = "D"
# else:
#     print("Grade E, Fail")
#
#
# print("Total score is: ", total_score)
# print("Avegrage marks: " ,avg)
# print("Total percentage: ",percentage)
# print("Your Grade is:", grade)
#
#
# # n1, n2, n3 = 37, 108, 67
# # average = (n1+ n2 + n3)/3
# # print(average)
# #
#
# from statistics import mean, median
# def improved_average(num):
#     print("The mean value: ", mean(num))
#     print("The median value: ", median(num))
#     return (num)
#
# num = (1, 2, 3, 4, 5)
# improved_average(num)


# =========================== ⬇️ Workshop 4 ⬇️ ===========================
# Develop a program that asks the user for a number and then displays whether the number is positive or negative.
# num = int(input("Enter a number: "))
# if num >=0:
#     print("The number you entered is positive.")
# else:
#     print("The number you entered is negative.")
# Part 2 1)	Develop a program that asks the user for a number and then displays whether the number is positive or negative.
# def num(n):
#     if n >= 0:
#         return "The number you entered is positive"
#     else:
#         return "The number you entered is negative"
# number = int(input("Enter a number: "))
# print(num(number))


# Part 2 Write a program that accepts percentage form the user and display the grade according to the following. [Percentage and GPA should be of herald college]
# Two ways
# 1st ⬇️
# percentage = float(input("Enter the marks: "))
# if (percentage > 90):
#     print("Grade A")
# elif (percentage > 80 and percentage <= 90):
#     print("Grade B")
# elif (percentage >= 60 and percentage <= 80):
#     print("Grade C")
# else:
#     print("Grade F")
# 2nd ⬇️
# def grade(percentage):
#     if (percentage > 90):
#         print("Grade A")
#     elif (percentage > 80 and percentage <= 90):
#         print("Grade B+")
#     elif (percentage >= 60 and percentage <= 80):
#         print("Grade B")
#     else:
#         print("Grade F")


# marks = float(input("Enter the marks: "))
# grade(marks)

# 3)	Write a program to check whether a year is a leap year or not.
# def leap_year(n):
#     if (n%4 == 0):
#         print(f"{n} is a leap year.")
#     else:
#         print(f"{n} is not a leap year.")
# year_name = int(input("Enter the year to check weather it is leap year or not: "))
# leap_year(year_name)
#

# 4)	 Write a program to check whether a person is eligible for voting or not. [voting age >= 18]
# def age(n):
#     if (n >= 18):
#         print(f"{n} is eligible for voting.")
#     else:
#         print(f"{n} is not eligible for voting.")
#
# person_age = int(input("Enter the person's age: "))
# age(person_age)

# 5)	Write a program to find the lowest number out of two numbers expected from the user
# def num(x, y):
#     if x < y:
#         print(f"{x} is the lowest number.")
#     else:
#         print(f"{y} is the lowest number.")
#
# num_1 = int(input("Enter the first number: "))
# num_2 = int(input("Enter the second number: "))
# num(num_1, num_2)

# 6)	Write a program to whether a number (accepted from user) is divisible by 2 and 3 both
# def num(n):
#     if (n%2==0) and (n%3==0):
#         print(f"{n} is divisible by 2 and 3 both.")
#     else:
#         print(f"{n} is not divisible by 2 and 3.")
# number = int(input("Enter a number: "))
# num(number)

# 7)	Write a program to check whether a character is a vowel or consonant. [expected from user’s input]
# def vowel(x):
#     # if x.lower() in ('a', 'e', 'i', 'o', 'u'):
#     if (x == 'a') or (x == 'e') or (x == 'i') or (x == 'o') or (x == 'u') or (x == 'A') or (x == 'E') or (x == 'I') or (x == 'O') or (x == 'U'):
#         print(f"{x} is a vowel letter.")
#     else:
#         print(f"{x} is a consonant letter")
# character = input("Enter a letter: ")
# vowel(character)
#
# 8)	Accept any city from the user and display tourist attractions of that city.
# City	Monuments
# Kathmandu	Pashupatinath Temple
# Pokhara	Fewa Lake
# Nepalgunj	Bageshwori Temple
# Birgunj	Birgunj Ghanta Ghar
#
# def city(city_name):
#     if (city_name == 'Kathmandu'):
#         print(f"Pashupatinath Temple is the reason for the attraction of Tourists in this {city_name} city.")
#     elif (city_name == 'Pokhara'):
#         print(f"Fewa Lake is the reason for the attraction of Tourists in this {city_name} city.")
#     elif (city_name == 'Nepalgunj'):
#         print(f"Bageshwori Temple is the reason for the attraction of Tourists in this {city_name} city.")
#     elif (city_name == 'Birgunj'):
#         print(f"Birgunj Ghanta Ghar is the reason for the attraction of Tourists in this {city_name} city.")
#     else:
#         print(f"{city_name} the city you entered does not have any information sorry.")
# name_of_city=input("Enter the name of the city: ")
# city(name_of_city)


# 9)	Accept the following from the user and calculate the percentage of class attended:
# a)	Total number of working days
# b)	Total number of absent days
# After calculating the percentage, if the percentage is less than 80,
# then students will not be able to sit the exam.
#
# total_working_days = int(input("Enter the total number of working days: "))
# absent_days = int(input("Enter the total number of absent days: "))
#
# attended_days = (total_working_days - absent_days)
# attendance_percentage = (attended_days / total_working_days) * 100
#
# def attendance_check(attendance_percentage):
#     if (attendance_percentage >= 80):
#         print(f"You can sit the exam. Your attendance percentage is {attendance_percentage:.2f}%.")
#     else:
#         print(f"You cannot sit the exam. Your attendance percentage is {attendance_percentage:.2f}%.")
#
# attendance_check(attendance_percentage)


# 10)Accept the marked price from the user and calculate the Net amount as (Marked Price - Discount) to pay according to the following criteria.

# marked_price = float(input("The marked price: "))
# discount = float(input("Enter the discount amount: "))
# discount_amount = (discount/100)
#
# net_amount = (marked_price-discount_amount)
# print(f"The net amount is {net_amount:.2f}")


# 11)	Evaluate the following expressions for num1 = 10 and num2 = 20.
# (a) not (num1 < 1) and num2 < 10
# (b) not (num1 < 1) and num2 < 10 or num1 + num3 < 100
# (c) not (num2 > 1) or num1 > num2 - 10

# num1 = 10
# num2 = 20
# num3 = (num1 + num2)
# def expression(num1, num2, num3):
#     expression_1 = not (num1<1) and (num2<10)
#     print(f"(a) expression_1 not ({num1} < 1) and ({num2} < 10) = {expression_1}")
#
#     expression_2 = not (num1<1) and (num2<10) or (num1 + num3 ) < 100
#     print(f"(b) expression_2 not ({num1} < 1) and ({num2} < 10) or ({num1}+{num3})<100 = {expression_2}")
#
#     expression_3 = not (num2 > 1) or (num1 > num2 - 10)
#     print(f"(c) expression_3 not ({num2} > 1) or ({num1} > {num2} - 10) = {expression_3}")
#
# expression(num1, num2, num3)

# 12)Write a program that takes three numbers as input and outputs the largest of the three numbers using if-else statements.
# For example, if the inputs are 4, 7, and 2, the program should output 7.
#
# x = int(input("Enter a first number: "))
# y = int(input("Enter a second number: "))
# z = int(input("Enter a third number: "))
#
# if (x>y) and (y>z):
#     highest =  x
# elif (y>x) and (y>z):
#     highest = y
# else:
#     highest = z
# print("The highest number is: ", highest)


# 14)	Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
#
# def difference(n):
#     if (n<=17):
#         return (17-n)
#     else:
#         return (n-17)*2
#
# n = int(input("Enter a number: "))
# print(difference(n))
#
# def add(a,b):
#     if ((a >= 15) and (b <= 20)):
#         print("The sum is",20)
#     else:
#         print("The sum is",a+b)
#
# x = int(input("Enter a 1st number: "))
# y = int(input("Enter a second number: "))
#
# add(x,y)


# 1. Write a Python function that takes two parameters, x and y, and returns the product of the two if they are both positive. If either x or y is negative, the function should return 0.

# def parameters(x,y):
#     if ((x>=0)and (y>=0)):
#         print(f"The product of the two number is: {x*y}")
#     else:
#         print("The number you entered is negative so its: 0")
# a = int(input("Enter a 1st number: "))
# b = int(input("Enter a 2nd number: "))
# parameters(a,b)
#

# 2.	Write a Python program that reads in two numbers and prints out whether their sum is even or odd.

# a = int(input("Enter a 1st number: "))
# b = int(input("Enter a 2nd number: "))
# def read(x,y):
#     if (x%2 == 0) and (y%2 == 0):
#         print(f"The sum is even: {x+y}")
#     else:
#         print(f"The sum is odd: {x+y}")
#
# read(a,b)

# 4.	 Rewrite the following if-else statements using a single if statement and elif:
# if temperature >= 85 and humidity > 60:
# print ('muggy day today')
# else:
# if temperature >= 85:
# print ('warm, but not muggy today')
# else:
# if temperature >= 65:
# print ('pleasant today')
# else:
# if temperature <= 45:
# print ('cold today')
# else:
# print ('cool today')
#
# temperature = int(input("Enter a temperature: "))
# humidity = int(input("Enter a temperature: "))
#
# if ((temperature >= 85) and (humidity >60)):
#     print("Muggy day today")
# elif (temperature >= 85):
#     print("Warm, but not muggy today")
# elif (temperature >= 65):
#     print("Pleasant today")
# elif (temperature <= 45):
#     print("Cold today")
# else:
#     print("Cool today")

#
# Give an appropriate if statement for each of the following.
# (The value of num is not important):
# (a) Displays 'within range' if num is between 0 and 100, inclusive.
# (b) Displays 'within range' if num is between 0 and 100, inclusive, and displays 'out of range' otherwise.
#
# #a)
# num = int(input("Enter a number: "))
# if num >= 0 and num <= 100:
#     print('Within range.')


# b)
# num = int(input("Enter a number: "))
# if num >= 0 and num <= 100:
#     print('within range')
# else:
#     print('out of range')
#


# 5.	 Write a Python program in which:
# (a) The user enters either 'A', 'B', or 'C'. If 'A' is entered, the program should display the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is entered, it displays 'Coconut'. Use nested if statements for this.

#
# 5.	 Write a Python program in which:
# (a) The user enters either 'A', 'B', or 'C'. If 'A' is entered, the program should display the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is entered, it displays 'Coconut'. Use nested if statements for this.
# for neseted
# letter = input("Enter either 'A', 'B', or 'C': ")
# if letter == 'A':
#     print('Apple')
# else:
#     if letter == 'B':
#         print('Banana')
#     else:
#         if letter == 'C':
#             print('Coconut')

# 5) b) Repeat question (a) using an if statement with elif headers instead.
# letter = input("Enter either A or B or C: ")
# if (letter == "A"):
#     print("Apple")
# elif (letter == "B"):
#     print("Banana")
# elif (letter == "C"):
#     print("Coconut")


# 5) (c) A student enters the number of college credits earned. If the number of credits is greater than or equal to 90, 'Senior Status' is displayed; if greater
# than or equal to 60, 'Junior Status' is displayed; if greater than or equal to 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed.

# college_credits = int(input("Enter the number of credits: "))
# def credits(n):
#     if (n>=90):
#         print("Senior Status")
#     elif (n>=60):
#         print("Junior Status")
#     elif (n>=30):
#         print("Sophomore Status")
#     else:
#         print("Freshman Status")
#
# credits(college_credits)

# 5) (d) The user enters a number. If the number is divisible by 3, the word ‘Fizz’ should be displayed; if the number is divisible by 5
# the word ‘Buzz’ should be displayed and if the number is divisible by both ‘FizzBuzz’ should be displayed.

# number = int(input("Enter a number: "))
# def num(n):
#     if (n%3 == 0) and (n%5==0):
#         print("FizzBuzz")
#     elif (n%3 == 0):
#         print("Fizz")
#     elif (n%5 == 0):
#         print("Buzz")
#
# num(number)

# Part 1
# 1.	How can you use logical operators (AND, OR, NOT) to combine multiple conditions in a control flow statement, and what are some common use cases for this type of logic?
# For AND logical operators
# a = 1
# b = 2
# c = 3
# if a < b and b < c:
#     print('Both conditions are true')
# else:
#     print('At least one condition is false')

# For OR logical operators
# x = 5
# y = 15
# z = 10
# if x < y or y < z:
#     print('At least one condition is true')
# else:
#     print('Both conditions are false')

# For NOT logical operators
# x = 5
# y = 10
#
# if not x > y:
#     print('x is not greater than y')
# else:
#     print('x is greater than y')


# Part 1
# 2.	What is a "nested control flow statement," and how can you use it to create more complex logic in your program?
# num = int(input("Enter a number: "))
# if num > 2:
#     print(f'The number {num} you entered is greater than 2')
#     if num > 4:
#         print(f'The number {num} you entered is also greater than 4')

# Part 1
# 3.	Describe the concept of "chaining" if-else statements together, and explain the advantages and disadvantages of this approach over using nested if statements.


# =========================== ⬇️ Week 5 Tutorail ⬇️ ===========================
# example
# number = int(input("Enter a number: "))
#
# while number !=0:
#     number = int(input("Enter a number: "))
#
# print("You Finally Pressed Zero: ")

# example 1
# i = 1
# n = 5
# while i<=n:
#     print(i)
#     i = i+1

# example
# number = int(input("Enter a number: "))
# sum = 0
# while number !=0:
#     sum = number + sum
#     number = int(input("Enter a number: "))
#
# print("The sum is:", sum)


# Example  ==========================
# while True:
#     num = int(input("Enter a number: "))
#     if num >=10:
#         print("Blah blah")
#         break
#     else:
#         print("Sorry")
#         continue


# Example
# for num in range (1, 6):
#     print(num)

# Example
# value = range(6)
# for i in value:
#     print(i)


# Define a variable n with the value 5
# n = 50
# # Use a "for loop" to iterate through a range of numbers from 0 to n-1
# for i in range(n):
#     # Calculate the number of spaces and stars needed for each row using the formulas n-i-1 and 2i+1
#     num_spaces = n - i - 1
#     # print('The num spaces', num_spaces)
#     num_stars = 2 * i + 1
#     # print('The num stars', num_stars)

#     # Use string concatenation to combine the spaces and stars into a single string for each row
#     row_string = ' ' * num_spaces + '*' * num_stars
#     # print('The row string', num_stars)

#     # Print out each row of the pyramid one by one
#     print(row_string)


# PART 4 (Home Task)
# You will need to understand control structures to complete the following questions. Therefore, you should carry out some independent research before attempting this. However, it will also be covered next week in class.
# 1. Create a function multiplication_table( ). It should take a single parameter n, which determines the size of the grid to be output e.g.
# multiplication_table(10)

# # def multiplication_table(n):
# #     for a in range(1, n+1):
# #         for b in range(1, n+1):
# #             print(a*b, end='\t')
# #         print()


# # number = int(input("Enter the size of the multiplication table: "))
# # multiplication_table(number)


# # 13)	Write a Python program that prompts the user to enter their weight in kilograms and their height in centimeters. The program should then calculate the user's BMI (Body Mass Index) using the formula: BMI = weight / height^2. The resulting BMI value should be printed to the console along with a message indicating whether the user is underweight (BMI < 18.5), normal weight (18.5 <= BMI < 25), overweight (25 <= BMI < 30), or obese (BMI >= 30).
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in cm: ")) / 100
# bmi = weight / height ** 2
# print("Your BMI is:", bmi)
# if (bmi < 18.5):
#     print("You are underweight.")
# elif (bmi < 25):
#     print(f"You are of normal.{bmi:.2f}")
# elif (bmi < 30):
#     print("You are overweight.")
# else:
#     print("You are obese.")


# Part 4
# Modify your existing function to take an additional parameter: power, with a default value of False. If a value of True is provided, your multiplication table should instead apply the top row as powers instead of multiplying the numbers.
# multiplication_table(3, True).

# def multiplication_table(n, power=False):
#     if power:
#         for a in range(1, n+1):
#             for b in range(1, n+1):
#                 print("{:4d}".format(a**b), end="")
#             print()
#     else:
#         for a in range(1, n+1):
#             for b in range(1, n+1):
#                 print("{:4d}".format(a**b), end="")
#             print()


# number = int(input("Enter the size of the multiplication table: "))
# multiplication_table(number, True)

# # =========================== ⬇️ Lab report 3 ⬇️ ===========================
# 1.Define a function either_side () which when passed an integer value also prints the values which are one less and one more than that value.# 1 number question
# def either_side(n):
#     print(n-1, n, n+1)


# number = int(input("Enter a number: "))
# either_side(number)

# 2.Add multi-line Docstrings to the function, create a simple function to take user input for “name”, “age” and Qualification.
# def your_name(name, age, qualification):
#     '''This is my multi-line docstrings to the function'''
#     print("Hi " + name + ". You are " + age + " years old. " +
#           qualification + " is your qualification")


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# qualification = input("Enter you qualification: ")
# print(your_name.__doc__)
# your_name(name, age, qualification)

# 3. Define a python function “avg” returns the average of three values (add 3 parameters, ex: x, y, z)
# def avg(x, y, z):
#     return (x + y + z) / 3


# result = avg(2, 3, 4)
# print(result)

# 4.	Write a Python function to find the maximum of three numbers.
# def max_of_three(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z


# result = max_of_three(2, 4, 6)
# print('The highest number is:', result)

# 5.Define a function string_to_int () that takes a string value and returns the sum after adding another integer value (make use of explicit conversion).
# def string_to_int(string_value, int_value):
#     return int(string_value) + int_value


# result = string_to_int("5", 3)
# print('The sum is', result)


# Calculator.
# def greet(name):
#     """Hello ,Welcome there!"""
#     print(greet.__doc__)
#     print(f"Lets get started,{name}!")


# greet("aryan")


# def add(x, y):
#     return x+y


# def subtract(x, y):
#     return x-y


# def divide(x, y):
#     return x/y


# def multiply(x, y):
#     return x*y


# def modulus(x, y):
#     return x % y


# def exponentiation(x, y):
#     return x**y


# print("Select the operation!")
# print("a.add")
# print("b.subtract")
# print("c.divide")
# print("d.multiply")
# print("e.modulus")
# print("f.exponentiation")
# print("q. quit")

# options = ""

# while options != "q":
#     options = input('please enter the options(a(for addition),b/c/d/e/f/q):')

#     if options != "q":
#         num1 = int(input("Enter the 1st number:"))
#         num2 = int(input("Enter the 2nd number:"))
#     if options == 'a':
#         print(num1, "+", num2, "=", add(num1, num2))
#     if options == 'b':
#         print(num1, "-", num2, "=", subtract(num1, num2))
#     if options == 'c':
#         print(num1, "/", num2, "=", divide(num1, num2))
#     if options == 'd':
#         print(num1, "*", num2, "=", multiply(num1, num2))
#     if options == 'e':
#         print(num1, "%", num2, "=", modulus(num1, num2))
#     if options == 'f':
#         print(num1, "**", num2, "=", exponentiation(num1, num2))
#     if options == 'q':
#         print('Your program has been terminated.')
#         break


# # =========================== ⬇️ Workshop 5 ⬇️ ===========================
# with function step
# 1.Write a program to print numbers from 1 to 10.
# def dips(n):
#     for i in range(1, n+1):
#         print(i)
# num = int(input("Enter the number that you wanted from 0 to your choice: "))
# dips(num)

# without function step
# for i in range(1, 11):
#     print(i)


# 2.Write a program to print all odd numbers between 1 and 15.
# def odd(n):
#     for i in range(1, n):
#         # for i in range(1, 16):
#         if i % 2 != 0:
#             print(i)


# num = int(input("Enter a number: "))
# odd(num)
# 3⬇️
# sum = 0
# for i in range(1, 11):
#     sum = sum+i
# print("The sum of the first 10 natural numbers: ", sum)
#
# 4⬇️
# Prompt the user to input a positive integer
# num = int(input("Enter a positive integer: "))

# print("Multiplication table of", num, ":")

# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)
#
# ⬇️5
# num = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, num+1):
#     factorial *= i

# print("The factorial of", num, "is", factorial)

#
# ⬇️6
# positive_count = 0
# negative_count = 0
# zero_count = 0

# while True:
#     num = int(input("Enter a number (or 0 to quit): "))

#     if num == 0:
#         break

#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1
#     else:
#         zero_count += 1

# print("Number of positive numbers entered:", positive_count)
# print("Number of negative numbers entered:", negative_count)
# print("Number of zeros entered:", zero_count)
#
# ⬇️7
# n = int(input("Enter the number of terms: "))

# a = 0
# b = 1

# print(a)
# print(b)

# for i in range(2, n):
#     c = a + b

#     print(c)

#     a = b
#     b = c

#
# ⬇️8
# string = input("Enter a string: ")

# reverse_string = string[::-1]

# print("The reversed string is:", reverse_string)

#
# ⬇️9
# for i in range(1, 8):
#     multiple = 7 * i

#     print(multiple)

#
# ⬇️10
# for i in range(1, 21):
#     if i % 5 == 0:
#         print(i * 5)
#         #
# for i in range(1, 21):
#     if i % 5 == 0:
#         print(i)
#
# ⬇️11
# for i in [2, 4, 5]:
#     print("Multiplication table of", i)

#     for j in range(1, 11):
#         print(i, "*", j, "=", i*j)

#     print()

#
# ⬇️12
# total = 0

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         total += i

# print("The sum of all numbers between 1 and 100 that are divisible by both 3 and 5 is:", total)

#
# ⬇️13
# total = 0

# for i in range(1, 101):
#     if i % 3 != 0 and i % 5 != 0:
#         total += i

# print("The sum of all numbers between 1 and 100 that are not divisible by 3 or 5 is:", total)

#
# ⬇️14
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()

#
# Part3 ⬇️1
# a⬇️
# sum = 0
# for num in range(100, 201):
#     if num % 2 == 0:
#         sum += num
# print("The sum of even numbers between 100 and 200 is:", sum)

# ⬇️ b
# sum = 0
# while True:
#     num = int(input("Enter a positive integer (or 0 to exit): "))
#     if num == 0:
#         break
#     elif num > 100:
#         continue
#     else:
#         sum += num
# print("The sum of the positive integers (excluding those greater than 100) is:", sum)

# c⬇️
# sum = 0
# num = 100
# while True:
#     if num > 200:
#         break
#     elif num % 2 == 1:
#         num += 1
#         continue
#     else:
#         sum += num
#         num += 2
# print("The sum of even numbers between 100 and 200 is:", sum)


#
# Part3 ⬇️2 solution
# product = 1
# num = int(input("Enter first number: "))
# while num != 0:
#     product *= num
#     num = int(input("Enter next number (0 to end): "))
# print("product =", product)

#
# Part3 ⬇️4
# num = int(input("Enter a number: "))
# largest_digit = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest_digit:
#         largest_digit = digit
#     num //= 10
# print("The largest digit is:", largest_digit)

#
# Part3 ⬇️5
# num = int(input("Enter a number: "))
# smallest_digit = 9
# while num > 0:
#     digit = num % 10
#     if digit < smallest_digit:
#         smallest_digit = digit
#     num //= 10
# print("The smallest digit is:", smallest_digit)

#
# Part3 ⬇️6
# string = input("Enter a string: ")
# vowel_count = 0
# for char in string:
#     if char in "aeiouAEIOU":
#         vowel_count += 1
# print("The number of vowels in the string is:", vowel_count)

#
# Part3 ⬇️7
# num = int(input("Enter a number: "))
# sum_of_digits = 0
# while num > 0:
#     digit = num % 10
#     # sum_of_digits += digit
#     sum_of_digits = sum_of_digits + digit
#     # num //= 10
#     num = num // 10
# print("The sum of the digits is:", sum_of_digits)

# ⬇️
# x = int(input("Enter the number: "))
# sum = 0

# while (x > 0):
#     result = x % 10
#     sum = sum+result
#     x = x//10
# print(sum)

#
# Part3 ⬇️8
# import random

# secret_number = random.randint(1, 20)
# num_guesses = 5
# guesses = []

# print("I'm thinking of a number between 1 and 20. You have 5 chances to guess the number.")

# for i in range(num_guesses):
#     guess = int(input("Guess a number: "))
#     guesses.append(guess)
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Congratulations, you guessed the number!")
#         break

# if guess == secret_number:
#     print("You guessed the number in", len(guesses), "guesses.")
# else:
#     print("Sorry, you ran out of guesses. The number was", secret_number)
#     print("Your guesses were:", guesses)
#
#
# Part 4⬇️ 1
# while True:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     operation = input(
#         "Enter operation addition(+), subtraction(-), multiplication(*), division(/) or 'e' to quit: ")

#     if operation == "+":
#         result = num1 + num2
#     elif operation == "-":
#         result = num1 - num2
#     elif operation == "*":
#         result = num1 * num2
#     elif operation == "/":
#         result = num1 / num2
#     elif operation == "e":
#         break
#     else:
#         print("Invalid operation. Please try again.")
#         continue

#     print(f"{num1} {operation} {num2} = {result}")
#
# Part 4⬇️2
# import random

# while True:
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice1 + dice2

#     guess = int(input("Guess the total value of the two dice (2-12): "))

#     if guess == total:
#         print("You guessed it right")
#     else:
#         print("Sorry, the actual total value was", total)

#     play_again = input("Do you want to play again? (y/n): ")

#     if play_again.lower() != 'y':
#         break

# print("Thanks for playing!")
#
# Part 4⬇️3
# import random

# rounds_played = 0
# wins = 0

# while True:
#     rounds_played += 1
#     print(f"\nRound {rounds_played}:")

#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice1 + dice2

#     guess = int(
#         input("Guess the total value of the two dice (2-12), or enter 0 to quit: "))

#     if guess == 0:
#         break

#     if guess == total:
#         print("Congratulations, you guessed correctly!")
#         wins += 1
#     else:
#         print(f"Sorry, the actual total value was {total}.")

#     win_percent = 100 * wins / rounds_played
#     print(
#         f"\nYou have won {wins} out of {rounds_played} rounds ({win_percent:.2f}%).\n")

# print("\nThanks for playing!")
#
# Part 1⬇️1
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in nested_list:
#     for j in i:
#         print(j)
#
# part 1⬇️1
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# for i in list1:
#     for j in list2:
#         print(i, j)
#
#

#
# # =========================== ⬇️ Tutorial 6 ⬇️ ===========================
# 1st example
# print("Natural number:")
# num = [1, 2, 3, 4, 5, 6, 7]
# print(num[2])

# 2nd example
# programming_language = ["Python", "Java", "AI"]
# print(programming_language)
# print(programming_language[0])
# programming_language[0] = 'C++'
# print(programming_language[0])
#
# append without loop 2 line below⬇️
# programming_language.append(True)
# print(programming_language)
#
# append⬇️
# programming_language = ["Python", "Java", "AI"]
# for i in range(0, len(programming_language)):
#     print(programming_language[i])
#     i = i+1
#
# append⬇️
# programming_language = ["Python", "Java", "AI"]
# for i in range(len(programming_language)):
#     print(programming_language[i])
#     i = i+1
#
# insert⬇️
# example
# programming_language = ["Python", "Java", "AI"]
# programming_language.insert(0, 1)
# print(programming_language)
#
# example⬇️
# programming_language = ["Python", "Java", "AI"]
# programming_language.insert(0, ["Dips"])
# print(programming_language)
#
# example⬇️
# programming_language = ["Python", "Java", "AI"]
# programming_language.insert(
#     1, [4, 5, 6, 7, "Dips", True, [10, 100, "Blah", False]])
# print(programming_language)
#
# example⬇️
# programming_language = ["Python", "Java", "AI"]
# programming_language.insert(
#     1, [4, 5, 6, 7, "Dips", True, [10, 100, "Blah", False]])
# print(programming_language)
# print(programming_language[1][6])
#
# example for loop⬇️
# programming_language = [["The Lost City", 2020],
#                         ["The Avatar", 2023], ["Iron Man", 2018]]
# for i in range(len(programming_language)):
#     print(programming_language[i])
#
# example without loop⬇️
# programming_language = [["The Lost City", 2020],
#                         ["The Avatar", 2023], ["Iron Man", 2018]]
# print(programming_language[1])
#
# Tuple ⬇️
# num = ("Dips", 1, [["The Lost City", 2020],
#                    ["The Avatar", 2023], ["Iron Man", 2018]], True, 'Bhattarai', "HCK")
# print(num[4])
# print(num[-1])
#
# example square ko lagi ⬇️
# number = [1, 2, 3, 4, 5, 6]
# square = [x**2 for x in number]
# print(square)
# for even
# even_num = [x for x in number if x % 2 == 0]
# print(even_num)
#
# # =========================== ⬇️ Lab report 4 ⬇️ ===========================
# 1.Write a program to calculate the electricity bill (accept number of units from user) according to the following criteria:
#        Unit                                                     Price
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
# ⬇️Solution
# def calculate_bill(units):
#     if units <= 100:
#         return 0
#     elif units <= 200:
#         return (units - 100) * 5
#     else:
#         return (units - 200) * 10 + 500


# units = int(input("Enter number of units: "))
# bill = calculate_bill(units)
# print(f"Total bill amount is Rs{bill}")
#
# 2.The user enters either 'A', 'B', or 'C'. If 'A' is entered, the program should display the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is entered, it displays 'Coconut'.
# ⬇️Solution
# def fruit(x):
#     if x == 'A':
#         print('Apple')
#     elif x == 'B':
#         print('Banana')
#     elif x == 'C':
#         print('Coconut')
#     else:
#         print('Invalid input')


# x = input("Enter a letter (A, B, or C): ")
# fruit(x)
#
# 3.Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
# ⬇️Solution
# def multiple(n):
#     if (n % 5 == 0):
#         print("Hello")
#     else:
#         print("Bye")


# number = int(input("Enter a number: "))
# multiple(number)
#
# 4. Write a program to check whether a person is eligible for citizenship or not. (Citizenship age >=18)
# ⬇️Solution:
# def check(age):
#     if age >= 18:
#         print("You are eligible for citizenship")
#     else:
#         print("You are not eligible for citizenship")


# age = int(input("Enter your age: "))
# check(age)
#
# 5.	Write a program to check whether a person is senior citizen or not, ask user age.
# ⬇️Soulution:
# Ask user for their age
# age = int(input("Please enter your age: "))

# if age >= 60:
#     print("You are a senior citizen.")
# else:
#     print("You are not a senior citizen yet.")
#
# 6.	Accept the age of 4 people and display the oldest one (take user input).
# ⬇️Solution
# Initialize the maximum age and oldest person's name
# max_age = 0
# oldest_person = ''

# # Ask for the age of each person and check if they are older than the current oldest person
# for i in range(4):
#     person_name = input(f"Enter name of person {i+1}: ")
#     person_age = int(input(f"Enter age of person {i+1}: "))
#     if person_age > max_age:
#         max_age = person_age
#         oldest_person = person_name

# # Display the name of the oldest person
# print(f"The oldest person is {oldest_person}, who is {max_age} years old.")
#
# # =========================== ⬇️ Lab report 5 ⬇️ ===========================
# 1.Python program to calculate the sum of all the odd and even numbers within the given range. (Suppose given range is 10)
# ➡️Solution
# # get the upper limit of the range from the user
# limit = int(input("Enter the upper limit of the range: "))

# # initialize variables to hold the sums of odd and even numbers
# odd_sum = 0
# even_sum = 0

# # loop through the range and add up the odd and even numbers
# for num in range(1, limit+1):
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num

# # print the results
# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)
#
# 2.	Write a program to print multiplication table of a given number using nested loop.
# ➡️Solution
# num = int(input("Enter a number: "))

# # # Nested loop to print the multiplication table
# for i in range(1, 11):
#     for j in range(1, num+1):
#         print("{:2d} x {:2d} = {:2d}".format(j, i, i*j), end="\t")
#     print()
#
# 3.Prompts the user to enter any number of positive and negative integer values, then displays the number of each type that were entered, sum the positive number (use break and continue concept).
# ➡️Solution
# positive_count = 0
# negative_count = 0
# positive_sum = 0

# while True:
#     num = int(input("Enter an integer (0 to quit): "))
#     if num == 0:
#         break
#     elif num > 0:
#         positive_count += 1
#         positive_sum += num
#     else:
#         negative_count += 1

# print("Number of positive integers entered:", positive_count)
# print("Number of negative integers entered:", negative_count)
# print("Sum of positive integers entered:", positive_sum)
#
# 4.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# ➡️Solution
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i)
#
# 5.	Use else block to display a message “Done” after successful execution of for loop. (Using while loop)
# ➡️ Solution
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Done")
#
# 6.	Write a program to fill up a general ENQUIRY FORM ask user input (name, age, qualification, contact number, address, email, interested area, description) at last ask them about salary expectations if their salary expectations are higher than 20k (display message, your work experience must be at least 2 years)
# if the experience is 2 or more years display (you are shortlisted your enquiry has been recorded, we will notify you, thank you!!)
# if the experience is less than 2 years and salary expectation is less than 20k display (your enquiry has been recorded, we will notify you, thank you!!)
# ➡️Solution
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# qualification = input("Enter your qualification: ")
# contact = input("Enter your contact number: ")
# address = input("Enter your address: ")
# email = input("Enter your email: ")
# area = input("Enter your interested area: ")
# description = input("Enter your description: ")
# salary_expectations = int(input("Enter your salary expectations: "))

# if salary_expectations > 20000:
#     experience = int(input("Enter your work experience in years: "))
#     if experience >= 2:
#         print("You are shortlisted. Your enquiry has been recorded. We will notify you. Thank you!!")
#     else:
#         print("Your work experience must be at least 2 years.")
# else:
#     print("Your enquiry has been recorded. We will notify you. Thank you!!")
#
# 6 kai using loop ⬇️
# while True:
#     name = input("Name: ")
#     age = input("Age: ")
#     qualification = input("Qualification: ")
#     contact_number = input("Contact Number: ")
#     address = input("Address: ")
#     email = input("Email: ")
#     interested_area = input("Interested Area: ")
#     description = input("Description: ")
#     salary_expectations = int(input("Salary Expectations: "))

#     if salary_expectations > 20000:
#         work_experience = int(input("Work Experience (in years): "))
#         if work_experience >= 2:
#             print(
#                 "You are shortlisted. Your enquiry has been recorded. We will notify you. Thank you!!")
#         else:
#             print("Your work experience must be at least 2 years.")
#     else:
#         print("Your enquiry has been recorded. We will notify you. Thank you!!")

#     another_enquiry = input("Do you want to submit another enquiry? (Y/N): ")
#     if another_enquiry.lower() == "n":
#         break
