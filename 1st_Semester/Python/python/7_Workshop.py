# Part 1 ⬇️ 1
# f = open("./Python/txt_file/7_Workshop.txt", "r")
# x = f.read()
# print(x)
# f.close()

# Part 1 ⬇️ 2
# output_file = open("./Python/txt_file/7_Workshop.txt", "w")
# x = output_file.write("Hello I changed the texts inside")
# print(x)
# output_file.close()

# Part 1 ⬇️ 3


# Part 1 ⬇️ 4
# input_file_opened = False
# while not input_file_opened:
#     try:
#         file_name = input("Enter file name: ")
#         input_file = open(file_name, "r")
#         print(input_file.read())
#         input_file.close()
#         input_file_opened = True
#     except:
#         print("File not found")


# Part 2 ⬇️ 1
# # this is written in the file
# # This line has extra space characters
# try:
#     f = open("./Python/txt_file/7_Workshop.txt", "r")
#     x = f.read()
#     y = x.split(" ")
#     print(y)
#     list_1 = []
#     for i in y:
#         list_1.append(i)
#     while ("") in list_1:
#         list_1.remove("")
#     print(list_1)
#     stri = ""
#     for j in list_1:
#         stri = stri+j+" "
#     print(stri)
# except:
#     print("Invalid name")


# Part 2 ⬇️ 2
# # this is written inside the file
# # The high today will be 75 degrees
# try:
#     f = open("./Python/txt_file/7_Workshop.txt", "r")
#     y = f.read()
#     f.close()
# except:
#     print("Invalid filename")


# def extract_temp(line):
#     x = y.split()
#     for i in x:
#         if (i.isdigit()):
#             print(i)
#         else:
#             pass
# extract_temp(y)


# Part 2 ⬇️ 3
# # this is written inside the file
# # Today’s high temperature will be 75 degrees
# try:
#     f = open("./Python/txt_file/7_Workshop.txt", "r")
#     x = f.read()
#     f.close()
#     print(x)
# except:
#     print("Invalid file name")


# def check_quotes(line):
#     quote = "Todayâ€™s high temperature will be 75 degrees"
#     x1 = quote.split(" ")
#     list_1 = []
#     for i in x1:
#         list_1.append(i)
#     list_2 = []
#     x2 = x.split(" ")
#     for j in x2:
#         list_2.append(j)
#     set1 = set(list_1)
#     set2 = set(list_2)
#     z = set1.issubset(set2)
#     return z

# Part 2 ⬇️ 1
# Part 2 ⬇️ 1
# """
# Part -1
# """
# # 1 Create a program in Python that opens a file named 'datafile.txt' for reading and assigns identifier input_file to the file object created.

# # input_file = open("datafile.txt", "r")
# # print(input_file.read())
# # input_file.close()


# # 2
# # try:
# #     output_file = open("datafile2.txt","w")
# #     output_file.write("Hello There How you doing!")

# # except  FileNotFoundError:
# #     print("The file does not exist.")

# # finally:
# #     output_file.close()

# # 3
# empty_str = ""
# input_file = open("./Python/txt_file/7_Workshop.txt", "r")
# output_file = open("./Python/txt_file/7_Workshop2.txt", "w")

# line = input_file.readline()
# while line != empty_str:
#     output_file.write(line+"\n")
#     line = input_file.readline()

# # 4

# # input_file_opened=False
# # while not input_file_opened:
# #     try:
# #         file_name=input("Enter file name: ")
# #         input_file=open(file_name,"r")
# #         input_file_opened=True
# #     except:
# #         print("File not found")

# # Part 2
# # 1
# def reduce_spaces(line):
#     return ' '.join(line.split())
# line = 'This line has   extra    space characters  '
# print(reduce_spaces(line))

# 2
# def extract_temp(line):
#     temp_str = ''
#     for char in line:
#         if char.isdigit():
#             temp_str += char
#         elif temp_str:
#             break
#     if temp_str:
#         return int(temp_str)
#     else:
#         return None
# line = 'The temperature is 25 degrees Celsius.'
# temp = extract_temp(line)
# if temp:
#     print('The temperature is:', temp) # Output: 'The temperature is: 25'
# else:
#     print('No temperature found.')

# 3
# def check_quotes(line):
#     stack = []
#     for char in line:
#         if char in ['"', "'"]:
#             if not stack or stack[-1] != char:
#                 stack.append(char)
#             else:
#                 stack.pop()
#     return len(stack) == 0
# line = "She said, 'I'm not sure if he'll come.'"
# if check_quotes(line):
#     print('All quotes are matched.')
# else:
#     print('There are unmatched quotes.')


# 4
# def count_letters(line):
#     freq = {}
#     for char in line.lower():
#         if char.isalpha():
#             freq[char] = freq.get(char, 0) + 1
#     return list(freq.items())


# line = 'This is a line'
# letter_freq = count_letters(line)
# print(letter_freq)

# 5
# def interleave_chars(line1, line2):
#     result = ''
#     for char1, char2 in zip(line1, line2):
#         result += char1 + char2
#     return result


# line1 = 'Hello'
# line2 = 'Goodbye'
# interleaved = interleave_chars(line1, line2)
# print(interleaved)

# 6

# line = 'This is a example line.\n'
# count = 0
# for char in line:
#     if char != ' ' and char != '\n':
#         count += 1
# print(count)

# 7. For variable month which contains the full name of any given month, give an expression to display just the first three letters of the month.

# month = 'September'
# short_month = month[:3]
# print(short_month)


# 8. Give an expression that displays True if the letter ‘r’ appears in a given month name stored in variable month, otherwise displays False.


# month = 'March'
# has_r = 'r' in month
# print(has_r)

# 9 Give an expression for determining how many times the letter ‘r’ appears in a given month name stored in variable month.
# month = 'December'
# r_count = month.count('r')
# print(r_count)

# 10
# first_name = "Dipesh"
# last_name = "Bhattarai"
# formatted_name = "{}, {}".format(last_name, first_name)
# print(formatted_name)

# 11. Give an instruction that determines if a given social security number represented as a string and stored in variable ss_num, contains any non- digits.

# ss_num = "123-00-1234"
# has_non_digits = not ss_num.isdigit()
# print(has_non_digits)


# 12. Give an instruction that determines the index of the ‘@’ character in an email address stored in variable email_addr.
# email_addr = "Dips.Bhattarai@example.com"
# at_index = email_addr.index('@')
# print(at_index)

# 13. For a variable named date containing a date in the form 12/14/2012, give an expression that replaces all slashes characters with dashes.


# date = '12/14/2012'
# new_date = date.replace('/', '-')
# print(new_date)

# 14. For a variable named err_mesg that contains error messages in the form ** error message **, give an expression that produces a string containing the error message without the leading and trailing asterisks and blank characters.

# err_mesg = '** Error message! **'
# msg = err_mesg.strip('* ').strip()
# print(msg)

#
# Part 3

# 1. Write a program that opens and reads a text file and displays how many lines of text are in the file.
# Open the file for reading
# with open('./Python/txt_file/7_Workshop.txt', 'r') as file:

#     contents = file.read().splitlines()

#     num_lines = len(contents)

#     print(f'The file contains {num_lines} lines of text.')

# 2. Write a program that reads a text file named original_text, and writes every other line, starting with the first line, to a new file named new_text.

# Open the original file for reading and the new file for writing

# with open('./Python/txt_file/7_Workshop.txt', 'r') as original_file, open('./Python/txt_file/7_Workshop2.txt', 'w') as new_file:

#     lines = original_file.readlines()

#     for i in range(0, len(lines), 2):
#         new_file.write(lines[i])

# 3. Write a program that reads a text file named original_text, and counts how many time the letter 'e' occurs (the most frequently occurring letter in English), and displays how many occurrences there are.

# filename = "./Python/txt_file/7_Workshop.txt"

# with open(filename, "r") as file:
#     count = 0
#     for line in file:
#         count += line.count("e")

# print("The file", filename, "contains",
#       count, "occurrences of the letter 'e'.")

# 4.  Write a program that reads a text file containing numerical expressions on
# each line and print them out along with the results. For example, for the numerical expression 4 + 2 in your file, your program should output: 4 + 2 = 6.


with open('./Python/txt_file/7_Workshop.txt', 'r') as file:
    for line in file:
        expression = line.strip()
        result = eval(expression)
        print(f"{expression} = {result}")
