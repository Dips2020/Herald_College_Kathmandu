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
