# f = open("./Python/txt_file/tutorial_6.txt", "r")
# print(f.read())
# # print(f.readline())


# # # to⬇️ open the file outside the main folder
# d = open('../Dipesh Bhattarai.txt', 'r')
# print(d.read())

# ⬇️while looping txt_file file
# file = open('./Python/txt_file/tutorial6.txt', 'r')
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# with⬇️ open for loop
# with open('./Python/txt_file/tutorial6.txt', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         print(line)

# ⬇️write
# file = open('./Python/txt_file/tutorial6.txt', 'w')
# file.write("Dipesh Bhattarai is in Herald College Kathamndu right now. \n")

# append
# file = open('./Python/txt_file/tutorial6.txt', 'a')
# file.write("Dipesh Bhattarai is in Herald College Kathamndu right now. \n")


# order
# ascii_value = ['a', 'b', 'c', 'A', 'B', 'C']


# for loop⬇️
# ascii_value = ['a', 'b', 'c', 'A', 'B', 'C']
# for i in ascii_value:
#     print(ord(i))


# using def function⬇️
# ascii_value = ['a', 'b', 'c', 'A', 'B', 'C']
# v = []
# def ascii(a):
#     for i in a:
#         v = ord(i)
#         return v
# value = ascii(ascii_value)
# print(value)


# for datatxt ⬇️
# checker = ""
# with open('datatxt', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         for w in word:
#             value = len(w)
#             if len(checker) < value:
#                 checker = w
# print(checker)
