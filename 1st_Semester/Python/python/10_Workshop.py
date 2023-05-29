
# ================= ⬇️ Part 1 ⬇️ =================
# ================= ⬇️ Part 2 ⬇️ =================
#  part 2 ⬇️ 1
# def sum_of_natural_numbers(n):
#     if n == 1:
#         return 1
#     return n + sum_of_natural_numbers(n - 1)
# def main():
#     n = int(input("Enter a positive integer: "))
#     if n <= 0:
#         print("Invalid input. Please enter a positive integer.")
#     else:
#         result = sum_of_natural_numbers(n)
#         print("The sum of the first", n, "natural numbers is:", result)
# main()

#  part 2 ⬇️ 2
# def get_input(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             return value
#         except ValueError:
#             print("Invalid input. Please enter a numeric value.")
# def main():
#     number = get_input("Enter a number: ")
#     print("The number you entered is:", number)
# main()

#  part 2 ⬇️ 3
# def main():
#     try:
#         number = int(input("Enter a positive integer: "))
#         if number <= 0:
#             raise ValueError("Invalid input. Please enter a positive integer.")
#         print("The number you entered is:", number)
#     except ValueError:
#         print("Please enter a integer.")
# main()


#  part 2 ⬇️ 4
# def replace_word(filename, old_word, new_word):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()

#         updated_content = content.replace(old_word, new_word)

#         with open(filename, 'w') as file:
#             file.write(updated_content)

#         print("Replacement complete.")
#     except FileNotFoundError:
#         print("File not found.")
# def main():
#     filename = input("Enter the filename: ")
#     old_word = input("Enter the word to replace: ")
#     new_word = input("Enter the new word: ")

#     replace_word(filename, old_word, new_word)
# main()


#  part 2 ⬇️ 5
# def is_text_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             return True
#     except IOError:
#         return False
# def handle_invalid_file(filename):
#     print(f"Error: {filename} is not a valid text file.")
# def main():
#     filename = input("Enter a filename: ")

#     if is_text_file(filename):
#         print(f"{filename} is a valid text file.")
#         # Continue processing the file
#     else:
#         handle_invalid_file(filename)
# main()

#  part 2 ⬇️ 6
# def binary_to_decimal(binary):
#     if len(binary) == 1:
#         return int(binary)
#     else:
#         # It will extract the last digit and it will convert it to an integer
#         last_digit = int(binary[-1])
#         # It removes the last digit from the binary number
#         remaining_binary = binary[:-1]
#         # Recursive call to convert the remaining binary number
#         decimal = binary_to_decimal(remaining_binary)
#         # It multiplies the decimal by 2 and add the last digit
#         decimal = decimal * 2 + last_digit
#         return decimal
# def main():
#     binary = input("Enter a binary number: ")
#     decimal = binary_to_decimal(binary)
#     print(f"The decimal equivalent of {binary} is: {decimal}")
# main()


#  part 2 ⬇️ 7
# def count_words_starting_with_vowel(filename):
#     vowel_count = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#                     vowel_count += 1
#     return vowel_count
# def main():
#     filename = input("Enter the filename: ")
#     try:
#         count = count_words_starting_with_vowel(filename)
#         print(
#             f"The number of words starting with a vowel in {filename} is: {count}")
#     except FileNotFoundError:
#         print(f"Error: {filename} not found.")
# main()


#  part 2 ⬇️ 8
# def is_list_unique(lst):
#     # Converting the list to a set and comparing the lengths
#     return len(lst) == len(set(lst))
# # Testing the function
# list1 = [1, 2, 3, 4, 5]
# print(is_list_unique(list1))
# list2 = [1, 2, 3, 3, 4, 5]
# print(is_list_unique(list2))
# list3 = ['a', 'b', 'c', 'd']
# print(is_list_unique(list3))
# list4 = ['a', 'b', 'c', 'c', 'd']
# print(is_list_unique(list4))


# ================= ⬇️ Part 3 ⬇️ =================
#  part 3 ⬇️ 1
# def display_tourist_attractions(city):
#     monuments = {
#         'Kathmandu': 'Pashupatinath Temple',
#         'Pokhara': 'Fewa Lake',
#         'Nepalgunj': 'Bageshwori Temple',
#         'Birgunj': 'Birgunj Ghanta Ghar'
#     }
#     if city in monuments:
#         print(f"The tourist attraction of {city} is: {monuments[city]}")
#     else:
#         print(f"No tourist monuments found for {city}.")
# def main():
#     city = input("Enter a city: ")

#     try:
#         display_tourist_attractions(city)
#     except KeyError:
#         print(f"Error: Invalid city '{city}' entered.")
# main()


#  part 3 ⬇️ 2
# def calculate_average(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average
# def main():
#     numbers = []
#     while True:
#         try:
#             value = input("Enter a number (or 'end' to finish): ")
#             if value.lower() == 'end':
#                 break

#             number = float(value)
#             numbers.append(number)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

#     if numbers:
#         average = calculate_average(numbers)
#         print(f"The average of the numbers is: {average}")
#     else:
#         print("No numbers entered.")
# main()


#  part 3 ⬇️ 3
# def calculate_sum(numbers):
#     total = sum(numbers)
#     return total
# def main():
#     numbers = []
#     while True:
#         try:
#             value = input("Enter an integer (or 'stop' to finish): ")
#             if value.lower() == 'stop':
#                 break

#             number = int(value)
#             numbers.append(number)
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")
#     if numbers:
#         total_sum = calculate_sum(numbers)
#         print(f"The sum of the integers is: {total_sum}")
#     else:
#         print("No integers entered.")
# main()


#  part 3 ⬇️ 4
# def compute_product(numbers):
#     if len(numbers) == 0:
#         return 1
#     else:
#         return numbers[0] * compute_product(numbers[1:])
# list1 = [1, 2, 3, 4]
# print(compute_product(list1))
# list2 = [1, 3, 5, 7]
# print(compute_product(list2))
# list3 = [10, 2, 5]
# print(compute_product(list3))

#  part 3 ⬇️ 5
# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n - 1)
# def main():
#     try:
#         n = int(input("Enter a positive integer: "))
#         if n < 0:
#             raise ValueError("Invalid input. Please enter a positive integer.")

#         factorial = calculate_factorial(n)
#         print(f"The factorial of {n} is: {factorial}")
#     except ValueError as e:
#         print(f"Error: {e}")
# main()


#  part 3 ⬇️ 6
# import csv


# def calculate_average_grade(file_path):
#     student_grades = {}

#     with open(file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             student_name = row['Name']
#             grade = float(row['Grade'])

#             if student_name in student_grades:
#                 student_grades[student_name].append(grade)
#             else:
#                 student_grades[student_name] = [grade]

#     for student, grades in student_grades.items():
#         average_grade = sum(grades) / len(grades)
#         print(f"Average grade for {student}: {average_grade:.2f}")


# csv_file_path = input("Enter the path to the CSV file: ")

# calculate_average_grade(csv_file_path)


#  part 3 ⬇️ 7
# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n - 1)
# def main():
#     while True:
#         try:
#             value = input("Enter a positive integer: ")
#             n = int(value)

#             if n < 0:
#                 raise ValueError(
#                     "Invalid input. Please enter a positive integer.")
#             factorial = calculate_factorial(n)
#             print(f"The factorial of {n} is: {factorial}")
#             break
#         except ValueError as e:
#             print(f"Error: {e}")
# main()


#  part 3 ⬇️ 8
# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     elif string[0] != string[-1]:
#         return False
#     else:
#         return is_palindrome(string[1:-1])
# def main():
#     user_input = input("Enter a string: ")

#     if is_palindrome(user_input):
#         print(f"The string '{user_input}' is a palindrome.")
#     else:
#         print(f"The string '{user_input}' is not a palindrome.")
# main()


#  part 3 ⬇️ 9
# import os
# def count_words(filename):
#     word_dict = {}
#     if not os.path.isfile(filename):
#         print("File does not exist.")
#         return word_dict
#     with open(filename, 'r') as file:
#         for line in file:
#             words = line.split()
#             # It will ppdate the word frequency in the dictionary
#             for word in words:
#                 word = word.lower()
#                 word_dict[word] = word_dict.get(word, 0) + 1
#     return word_dict
# def main():
#     filename = input("Enter the filename: ")
#     word_dict = count_words(filename)

#     if word_dict:
#         print("Word frequencies:")
#         for word, frequency in word_dict.items():
#             print(f"{word}: {frequency}")
# main()


#  part 3 ⬇️ 10
# def greatest_common_divisor(x, y):
#     if y == 0:
#         return x
#     return greatest_common_divisor(y, x % y)
# def get_input(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value <= 0:
#                 print("Please enter a positive integer.")
#             else:
#                 return value
#         except ValueError:
#             print("Invalid input. !! Please enter an integer.")
# def main():
#     print("Greatest Common Divisor Calculator")
#     print("Enter two positive integers.")
#     while True:
#         num1 = get_input("Enter the first integer: ")
#         if num1 > 0:
#             break
#     while True:
#         num2 = get_input("Enter the second integer: ")
#         if num2 > 0:
#             break
#     result = greatest_common_divisor(num1, num2)
#     print(f"The greatest common divisor of {num1} and {num2} is: {result}")
# main()

# ================= ⬇️ Part 4 ⬇️ =================
def read_sales_data(file_name):
    sales_data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                product_id, product_name, category, units_sold, unit_price = line.strip().split(',')
                sales_data.append({
                    'ProductID': product_id,
                    'ProductName': product_name,
                    'Category': category,
                    'UnitsSold': int(units_sold),
                    'UnitPrice': float(unit_price)
                })
        return sales_data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []


def calculate_revenue(sales_data):
    total_revenue = 0
    for product in sales_data:
        units_sold = product['UnitsSold']
        unit_price = product['UnitPrice']
        revenue = units_sold * unit_price
        total_revenue += revenue
    return total_revenue


def calculate_units_sold(sales_data):
    total_units_sold = 0
    for product in sales_data:
        units_sold = product['UnitsSold']
        total_units_sold += units_sold
    return total_units_sold


# Read the sales data from the file
sales_file = input("Enter a filename: ")
data = read_sales_data(sales_file)
# Calculate the total revenue and units sold
total_revenue = calculate_revenue(data)
total_units_sold = calculate_units_sold(data)
# Creating the report
print("-------------------------")
print("Sales Report")
print("-------------------------")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Total Units Sold: {total_units_sold}")
print("-------------------------")
