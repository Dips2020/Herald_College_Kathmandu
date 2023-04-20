# 1. ⬇️	Write a Python program to read an entire text file.
# file = open('./Python/txt_file/week7_lab.txt', 'r')
# data = file.read()
# print(data)
# file.close()


# 2.⬇️	Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.
# file = open('./Python/txt_file/PYTHON.TXT', 'r')
# data = file.read()
# count = 0
# for char in data:
#     if char.isupper():
#         count = count + 1
# print("Number of uppercase alphabets in the file: ", count)
# file.close()


# 3.⬇️	Write a program which uses (file read using "open ()" & "with open ()") both.
# # Using open() method
# file1 = open("./Python/txt_file/week7_lab.txt", "r")
# data1 = file1.read()
# print(f"Using open() method:\n{data1}")
# file1.close()

# # Using with open() method
# with open("./Python/txt_file/week7_lab.txt", "r") as file2:
#     data2 = file2.read()
#     print(f"\nUsing with open() method:\n{data2}")
#     # The file is automatically closed after the 'with' block is executed


# 4.⬇️Write a Python program to write a list content to a file. (Sample list (color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
# # Create a list of items to be written to the file
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open("./Python/txt_file/week7_lab.txt", "w") as file:
#     for item in color:
#         file.write(item + "\n")
# file.close()


# 5.⬇️Write a Python program that reads a text file named "data.txt" and finds the longest word in the file. The program should use a loop to read each line of the file, split each line into words using the split () method, and then iterate over each word to find the longest one. Once the loop has finished, the program should print the longest and shortest and equal length words found in the file.
# with open("./Python/txt_file/week7_lab.txt", "r") as file:
#     # Initialize variables to store the longest, shortest, and equal length words
#     longest_word = ""
#     shortest_word = ""
#     equal_length_words = []

#     # Iterate through each line of the file
#     for line in file:
#         # Split each line into words
#         words = line.split()

#         # Iterate over each word and find the longest, shortest, and equal length words
#         for word in words:
#             if len(word) > len(longest_word):
#                 longest_word = word
#             # elif len(word) < len(shortest_word) or shortest_word == "":
#             elif len(word) < len(shortest_word) or shortest_word == "":
#                 shortest_word = word
#             elif len(word) == len(longest_word) or len(word) == len(shortest_word):
#                 equal_length_words.append(word)

#     # Print the longest, shortest, and equal length words found in the file
#     print("Longest Word: ", longest_word)
#     print("Shortest Word: ", shortest_word)
#     print("Equal Length Words: ", equal_length_words)


# 6.⬇️Write a python program to save a simple inquiry form data to a file name called formdata.txt. Form details (name, age, qualification, description, hobby, and interest, etc.)
name = input("Enter your name: ")
age = input("Enter your age: ")
qualification = input("Enter your qualification: ")
description = input("Enter a short description about yourself: ")
hobby = input("Enter your hobby: ")
interest = input("Enter your interests: ")

data = {
    "Name": name,
    "Age": age,
    "Qualification": qualification,
    "Description": description,
    "Hobby": hobby,
    "Interest": interest
}
# write the user's data to a file
with open("./Python/txt_file/7lab_formdata.txt", "w") as file:
    for key, value in data.items():
        file.write(f"{key}: {value}\n")
print("Your data has been saved to formdata.txt")
