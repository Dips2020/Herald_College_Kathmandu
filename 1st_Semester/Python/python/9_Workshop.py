#
#
#
# =============== Part 1 ⬇️ ===============
# QNo. 4 ⬇️
# age = input("Enter your age: ")
# if not age.isdigit():
#     raise ValueError("Invalid age: Your age must be a positive number.")
# print("Your age is:", age)

# =============== Part 2 ⬇️ ===============
# QNo. 1 ⬇️
# def division_operation():
#     try:
#         num1 = int(input("Enter 1st integer: "))
#         num2 = int(input("Enter 1st integer: "))
#         calculation = num1/num2
#         print("The result is:", calculation)

#         # print("The result is:{:.2f}".format(calculation))
#         # print(f"The result is:{calculation:.2f}")
#     except ValueError:
#         print("Enter a valid integer.")
#     except ZeroDivisionError as z:
#         print(f"Opps! An Error Occured: {z}")
# division_operation()

# QNo. 2 ⬇️
# def file_open():
#     try:
#         file_path = input("Enter a filename: ")
#         with open(file_path, "r") as file:
#             data = file.read()
#             print(data)
#     except FileNotFoundError:
#         print("File not found.")
#     except PermissionError:
#         print("Oops! Permission denied.")
#     except EOFError as e:
#         print("Oops! An Error Occurred.", e)
# file_open()

# QNo. 3 ⬇️
# def list_num():
#     list_num = []
#     user_input = input("Enter a list_num of list_num separated by spaces: ").split()
#     for num in user_input:
#         try:
#             number = float(num)
#             list_num.append(number)
#         except ValueError:
#             print(f"Invalid input: {num} is not a number.")
#     try:
#         average = sum(list_num) / len(list_num)
#         print("The average of the list_num is:", average)
#     except ZeroDivisionError:
#         print("No numbers were entered.")
# list_num()

# QNo. 4 ⬇️
# import random
# guess_num = random.randint(1, 10)
# while True:
#     try:
#         guess = int(input("Guess the number between 1 and 10: "))
#         if guess < 1 or guess > 10:
#             raise ValueError(
#                 "Your guess is out of range. Please enter a number between 1 and 10."
#             )
#         break
#     except Exception as e:
#         print("Invalid input:", e)

# if guess == guess_num:
#     print("Congratulations! You guessed the secret number.")
# else:
#     print(
#         f"Oops! the secret number was {guess_num}. Better luck next time!")

# QNo. 5 ⬇️
# numbers = []
# while True:
#     try:
#         num = input("Enter an integer (or 'e' to finish): ")
#         if num.lower() == "e":
#             break
#         numbers.append(int(num))
#     except ValueError:
#         print("Invalid input. Please enter an integer or 'done' to finish.")
# print("The sum of the numbers is:", sum(numbers))

# QNo. 6 ⬇️
# try:
#     num1 = int(input("Enter a 1st num: "))
#     num2 = int(input("Enter a 2nd num: "))
#     result = num1 / num2
#     print("The result is:", result)
# except ZeroDivisionError as e:
#     print("Oops!", e)

# QNo. 7 ⬇️
# simple_list = [1, 2, 3, 4, 5]
# try:
#     index_num = int(input("Enter a index number: "))
#     print("list_num data:", simple_list[index_num])
# except IndexError as e:
#     print("Oops!", e)

# QNo. 8 ⬇️
# try:
#     index_num = int(input("Enter a index number: "))
#     print("list_num data:", simple_list[index_num])
# except IndexError as e:
#     print("Oops!", e)
# except NameError as e:
#     print("Oops! Problem:", e)

# QNo. 9 ⬇️
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input. Please enter an integer.")
# else:
#     print("The square of", num, "is", num*num)

# QNo. 10 ⬇️
# a = int(input("Enter a 1st num: "))
# b = int(input("Enter a 2nd num: "))
# try:
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     else:
#         print(a / b)
# except ZeroDivisionError as e:
#     print("Error:", e)


# =============== Part 3 ⬇️ ===============
# QNo. 1 ⬇️
# while True:
#     try:
#         str_num = input("Enter a number: ")
#         int_num = int(str_num)
#         break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")

# print("The number entered is:", int_num)


# QNo. 2 ⬇️
# try:
#     numerator_num = int(input("Enter a numerator number: "))
#     denominator_num = int(input("Enter a denominator number: "))
#     result = numerator_num / denominator_num
#     print(f"The result:{result:.2f}")
# except ZeroDivisionError:
#     print("Can't divide by zero.")
# except ValueError:
#     print("Entered value is wrong.")

# QNo. 3 ⬇️
# try:
#     money = int(input("Enter the amount of money: "))
#     if money < 10000:
#         raise ValueError("Insufficient balance.")
#     print("Wow!, you have sufficient balance:", money)
# except ValueError as e:
#     print("Invalid input.", e)

# QNo. 4 ⬇️
# try:
#     name = input("Enter your name: ")
#     if not name:
#         raise EOFError("No input received")
#     print("Your name is:", name)
# except EOFError as e:
#     print("An EOFError occurred:", e)

# QNo. 5 ⬇️
# def largest_integer(list_num):
#     """
#     This function takes a list_num of integers as input and returns the largest integer in the list_num.
#     If the input list_num is empty, it raises a ValueError.
#     """
#     if len(list_num) == 0:
#         raise ValueError("List cannot be empty")
#     # Initialize the maximum element as the first element of the list_num
#     max_num = list_num[0]
#     # Loop through the list_num, comparing each element to the current maximum
#     for number in list_num:
#         if number > max_num:
#             max_num = number
#     return max_num


# input_str = input("Enter a list_num of integers separated by space: ")
# # Split the input string into a list_num of individual strings
# input_list = input_str.split()
# # Convert each string in the list_num to an integer
# list_num = []
# for num_str in input_list:
#     num = int(num_str)
#     list_num.append(num)
# # Call the find_largest_integer() function
# try:
#     largest_int = largest_integer(list_num)
#     print(f"The largest integer in the list_num {list_num} is: {largest_int}")
# except ValueError as e:
#     print(f"Error: {e}")


# QNo. 5 final ⬇️
# def largest_integer(list_num):
#     if len(list_num) == 0:
#         raise ValueError("list_num should not be empty")
#     max_num = list_num[0]
#     for number in list_num:
#         if number > max_num:
#             max_num = number
#     return max_num


# user_num = input("Enter a list_num of integers separated by space: ")
# input_list = user_num.split()

# list_num = []
# for user_number in input_list:
#     num = int(user_number)
#     list_num.append(num)

# try:
#     largest_int = largest_integer(list_num)
#     print(f"The largest integer in the list_num {list_num} is: {largest_int}")
# except ValueError as e:
#     print(f"Error: {e}")


# QNo. 6 ⬇️
# def dictionary_value(dict_data, key):
#     """
#     This function takes a dictionary and a key as input and returns the value associated with the key.
#     If the key does not exist in the dictionary, it raises a KeyError.
#     """
#     try:
#         return dict_data[key]
#     except KeyError:
#         raise KeyError(f"Key '{key}' does not exist in the dictionary")


# try:
#     my_dict = {"Dipesh": 6, "Herald": 5, "Wolverhampton": 13}
#     key = "Dipesh"
#     value = dictionary_value(my_dict, key)
#     print(f"The value associated with a given key '{key}' is {value}")

#     key = "College"
#     value = dictionary_value(my_dict, key)
#     print(f"The value associated with a given key '{key}' is {value}")
# except KeyError as e:
#     print(f"Error: {e}")

# QNo. 7 ⬇️
# def concatenate_strings(str1, str2):
#     try:
#         result = str1 + str2
#     except TypeError:
#         result = "Error: One or both arguments are not strings"
#     return result


# # Example 1: Concatenating two strings
# str1 = "Hello"
# str2 = "World"
# concatenated_string = concatenate_strings(str1, str2)
# print(concatenated_string)  # Output: HelloWorld

# # Example 2: Concatenating a string and a non-string
# str1 = "Hello"
# non_str = 123
# concatenated_string = concatenate_strings(str1, non_str)
# # Output: Error: One or both arguments are not strings
# print(concatenated_string)

# QNo. 7 final ⬇️
# def concatenate_strings(str1, str2):
#     try:
#         result = str1 + str2
#     except TypeError:
#         result = "O0ps! argument is not a string."
#     return result


# str1 = "Dipesh"
# str2 = "Bhattarai"
# concatenated_string = concatenate_strings(str1, str2)
# print(concatenated_string)

# str1 = "Herald"
# non_str = 977
# concatenated_string = concatenate_strings(str1, non_str)
# print(concatenated_string)


# =============== Part 4 ⬇️ ===============
# student_names = []
# student_grades = {}

# while True:
#     try:
#         num_students = int(
#             input("Enter the total number of students in the class: "))
#         break
#     except ValueError:
#         print("Oops! please enter the number.")

# for i in range(num_students):
#     while True:
#         try:
#             name = input("Enter the name of student {}: ".format(i+1))
#             if not name.isalpha():
#                 raise ValueError
#             break
#         except ValueError:
#             print("Wrong name. Please enter a string.")

#     student_names.append(name)

#     while True:
#         try:
#             grade = float(input("Enter the grade for {}: ".format(name)))
#             if 0 <= grade <= 100:
#                 student_grades[name] = student_grades.get(name, []) + [grade]
#                 break
#             else:
#                 print("Grade value must be between 0-100.")
#         except ValueError:
#             print("Invalid grade value. Please enter a number.")

# # Initialize an empty list to store the average grades for each student
# average_grades = []

# # Loop over each student's name in the list of student names
# for name in student_names:

#     # Get the list of grades for this student from the dictionary of student grades
#     grades = student_grades.get(name, [])

#     # Calculate the average grade for this student using the sum() and len() functions
#     # If the list of grades is empty, set the average grade to 0 to avoid division by 0
#     if grades:
#         avg_grade = sum(grades) / len(grades)
#     else:
#         avg_grade = 0

#     # Add the average grade to the list of average grades
#     average_grades.append(avg_grade)

#     # Print the student's name and average grade with two decimal places using the format() function
#     print("{}'s average grade: {:.2f}".format(name, avg_grade))

# # Calculate the class average grade by summing the list of average grades and dividing by the number of students
# # If there are no students, set the class average grade to 0 to avoid division by 0
# class_avg = sum(average_grades) / num_students if num_students else 0

# # Print the class average grade with two decimal places using the format() function
# print("Class average grade: {:.2f}".format(class_avg))
#
#
#
# Part 4 final ⬇️
student_names = []
student_grades = {}
while True:
    try:
        num_students = int(
            input("Enter the total number of students in the class: "))
        break
    except ValueError:
        print("Oops! please enter the number.")
for i in range(num_students):
    while True:
        try:
            name = input("Enter the name of student {}: ".format(i+1))
            if not name.isalpha():
                raise ValueError
            break
        except ValueError:
            print("Wrong name. Please enter a string.")

    student_names.append(name)
    while True:
        try:
            grade = float(input("Enter the grade for {}: ".format(name)))
            if 0 <= grade <= 100:
                student_grades[name] = student_grades.get(name, []) + [grade]
                break
            else:
                print("Grade value must be between 0-100.")
        except ValueError:
            print("Invalid grade value. Please enter a number.")
# Initializing an empty list to store the average grades for each student
average_grades = []
# Looping over each student's name in the list of student names
for name in student_names:
    # Get the list of grades for this student from the dictionary of student grades
    grades = student_grades.get(name, [])
    # Calculate the average grade for this student using the sum() and len() functions
    # If the list of grades is empty, set the average grade to 0 to avoid division by 0
    if grades:
        avg_grade = sum(grades) / len(grades)
    else:
        avg_grade = 0
    # Add the average grade to the list of average grades
    average_grades.append(avg_grade)
    # Print the student's name and average grade with two decimal places using the format() function
    print("{}'s average grade: {:.2f}".format(name, avg_grade))
# Calculate the class average grade by summing the list of average grades and dividing by the number of students
# If there are no students, set the class average grade to 0 to avoid division by 0
class_avg = sum(average_grades) / num_students if num_students else 0
# Print the class average grade with two decimal places using the format() function
print("Class average grade: {:.2f}".format(class_avg))
