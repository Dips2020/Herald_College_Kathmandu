# ➡️1st
# try:
#     num1 = int(input("Enter a first number: "))
#     num2 = int(input("Enter a second number: "))

#     # sum = num1 + num2
#     sum = num1 / num2
#     print(sum)

# except:
#     # print("Invalid number")
#     '''ZeroDivisionError exception'''
#     print("Error: Denominator cannot be zero")

# ➡️2
# try:
#     # with open("sth.txt", "r") as file:
#     with open("./Python/txt_file/9_Tutorial.txt", "r") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("File access denied.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# ➡️3
# try:
#     choice = int(input('Enter a number: '))
#     assert choice > 0
# except AssertionError:
#     print("Number is negative")
# except Exception as e:
#     print(f"An error occured: {e}")

# ➡️4
