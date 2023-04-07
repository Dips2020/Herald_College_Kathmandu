# f = open('./text/tutorial6.text', 'r')
# # print(f.read())
# print(f.readline())


# to⬇️ open the file outside the folder
# d = open('../Dipesh bhattarai.txt', 'r')
# print(d.read())

# ⬇️while looping text file
# file = open('./text/tutorial6.text', 'r')
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# with⬇️ open for loop
# with open('./text/tutorial6.text', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         print(line)

# ⬇️write
# file = open('./text/tutorial6.text', 'w')
# file.write("Dipesh Bhattarai is in Herald College Kathamndu right now. \n")

# append
# file = open('./text/tutorial6.text', 'a')
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


# for data.text ⬇️
# checker = ""
# with open('data.text', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         for w in word:
#             value = len(w)
#             if len(checker) < value:
#                 checker = w
# print(checker)
