
# ⬇️ 1
# main.py
# this module does not exist in the current directory or in the Python path
# import Dipesh

# print("Dipesh")

# # try:
# #     import Dipesh
# # except ModuleNotFoundError:
# #     print("Module Dipesh not found")


# ⬇️ 2
# try:
#     # This is ZeroDivisionError
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(f"This is ZeroDivisionError: {e}")

# try:
#     # This is ValueError
#     x = int("abc")
# except ValueError as e:
#     print(f"This is ValueError: {e}")

# try:
#     # This is a global exception
#     x = "1" + 1
# except Exception as e:
#     print(f"This is a global exception {type(e).__name__}: {e}")

# ⬇️ 3
# try:
#     num = int(input("Enter a number: "))

#     value = 100 / num

# except ValueError:
#     print("You should enter a valid integer.")

# except ZeroDivisionError:
#     print("You cannot divide by zero.")

# else:
#     print(f"The result is {value:.2f}")

# finally:
#     print("Try again.")


# ⬇️ 4
# try:
#     num1 = int(input("Enter a first number: "))
#     num2 = int(input("Enter a second number: "))
#     result = num1 / num2
#     print("The final result is:", result)

# except Exception as e:
#     print("Oops! An error occurred:", e)

# ⬇️ 5
# def divide_num(num1, num2):

#     if num2 == 0:
#         raise ValueError("The second number cannot be zero!")
#     else:
#         return num1 / num2


# try:
#     num1 = int(input("Enter 1st num: "))
#     num2 = int(input("Enter 2nd num: "))
#     result = divide_num(num1, num2)
#     print("The result is:", result)

# except ValueError as e:
#     print("Oops! An exception occurred:", e)


# ⬇️ 6
# fruits = ['herald', 'Dips', 'Python']

# try:
#     print(fruits[3])
# except IndexError as e:
#     print("Oops! An exception occurred:", e)


# ⬇️ 7
# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             data = f.read()
#             print("File contents:", data)
#     except FileNotFoundError as e:
#         print("Oops! File not found.")
#         print("Exception message:", e)
#     except PermissionError as e:
#         print("Oops! Permission denied.")
#         print("Exception message:", e)
#     except EOFError as e:
#         print("Oops! Out of reach.")
#         print("Exception message:", e)


# file_path = input("Enter a filename: ")
# try:
#     read_file(file_path)
# except Exception as e:
#     print("Oops! An exception occurred:", e)


# ⬇️ 8
def guess_car():
    car_list = ["honda", "tesla", "lambo"]
    try:
        guess = input("Guess the car brand from this list: " +
                      str(car_list) + "\n").lower()
        if guess in car_list:
            print("Congratulations, you guessed the car brand!")
        else:
            print("Sorry, your guess was not correct.")
    except Exception:
        print("Oops! An exception occurred:")


guess_car()
# tala ⬇️ it works too
# try:
#     guess_car()
# except Exception as e:
#     print("Oops! An exception occurred:", e)
