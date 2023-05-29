# # =========================== ⬇️ Practice Qestion⬇️ ===========================
# B. Write a program to paint a fence at 30rs per square feet asking the length and breadth to the user in feet and also price of painting.
# Question 1 ⬇️ B->Solution ⬇️
# lenght = float(input("Enter the lenght of the fence: "))
# breadth = float(input("Enter the breadth of the fence: "))
# area = (lenght * breadth)
# price = (area*30)
# print("The price of painting the fence is: Rs", price)


# B. Write a program to find the greatest of 3 numbers where the numbers are provided by the users.
# Question 2 ⬇️ B->Solution ⬇️
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the greatest number")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is the greatest number")
# else:
#     print(f"{num3} is the greatest number")


# C. Write a Python program that prompts the user to enter a password and checks if it meets certain requirements, such as being at least 8 characters long,  containing at least one uppercase letter, one lowercase letter, and one digit.
# Question 2 ⬇️ C->Solution ⬇️
# password = input("Enter a password: ")
# if len(password) < 8:
#     print("Password is too short. It must contain at leat 8 characters long.")
# elif not any(char.isdigit() for char in password):
#     print("Password must contain at least one digit.")
# elif not any(char.islower() for char in password):
#     print("Password must contain at least one lowercase letter.")
# elif not any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter.")
# else:
#     print("Password meets all requirements.")


# B. Make a rug of ‘#’ where the row and column of rug is given by the users through parameters.
# Question 3 ⬇️ B->Solution ⬇️
# def make_rug(rows, colums):
#     for i in range(rows):
#         for j in range(colums):
#             print('*', end="")
#         print()
# rows = int(input("Enter the number of rows: "))
# colums = int(input("Enter the number of colums: "))
# make_rug(rows, colums)


# C. Write a Python program that uses a loop to repeatedly prompt the player to guess the total value of two dice, generate random dice rolls, compare the rolls to the guess, and display the result. The program should continue looping until the player chooses to quit the game. At the end of each round, the program should display the number of rounds played and the player's win percentage.
# Question 3 ⬇️ C->Solution ⬇️
# import random
# rounds_played = 0
# num_wins = 0
# while True:
#     guess = int(
#         input("Guess the total number between 2 and 12 or enter 0 to quit: "))
#     if (guess == 0):
#         break
#     if (guess < 2) or (guess > 12):
#         print("Invalid guess. Please enter the number between 2 and 12.")
#         continue
#     roll_1 = random.randint(1, 6)
#     roll_2 = random.randint(1, 6)
#     total_roll = (roll_1 + roll_2)
#     print("The total dice roll:", total_roll)
#     if (total_roll == guess):
#         print("You win!.")
#         num_wins = (num_wins + 1)
#     else:
#         print("Sorry you lose.!")
#     rounds_played = (rounds_played + 1)
#     print("The total rounds played:", rounds_played)
#     win_percentage = (num_wins / rounds_played * 100)
#     print(f"Win percentage: {win_percentage:.2f}%")


# B. Write a program to change the key value pair of existing dictionary.
# Question 4 ⬇️ B->Solution ⬇️
# Create a dictionary

# Create a dictionary
# my_dict = {"apple": 2, "banana": 4, "orange": 6}

# # Print the original dictionary
# print("Original Dictionary:")
# print(my_dict)

# # Change the key "apple" to "pear" and its value to 8
# my_dict["pear"] = my_dict.pop("apple", 0)
# print("Updated Dictionary:")
# print(my_dict)


# Question 5 ⬇️ B->Solution ⬇️
# create a 3x3 matrix filled with 1's
# matrix = [[1, 1, 1],
#           [1, 1, 1],
#           [1, 1, 1]]

# # prompt the user to input a row and column number
# row = int(input("Enter the row number (0-2): "))
# col = int(input("Enter the column number (0-2): "))

# # update the matrix with the user's input
# matrix[row][col] = "X"

# # print the updated matrix
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end=" ")
#     print()
