# # =========================== ⬇️ Workshop 6 ⬇️ ===========================
# ⬇️Exercise 2 --- 1
# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)
# print(my_list)

# ⬇️Exercise 2----2
# my_list = [["apple", "banana", "cherry"], [
#     "dog", "cat", "bird"], ["red", "green", "blue"]]

# print(my_list[2][0])

# ⬇️Exercise 2 ---3
# my_tuple = (1, 2, 3, 4, 5)
# # my_tuple = ("Dipesh Bhattarai")

# print(len(my_tuple))

# ⬇️Exercise 2 ---4
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)


# ⬇️Exercise 2 ---5
# student_dict = {"Dips": 18, "Toothless": 20, "Ironman": 19, "Superman": 22}

# print(student_dict["Superman"])


# ⬇️Exercise 2 ---6
# num_list = input("Enter a list of integers, separated by spaces: ").split()

# num_list = ['over' if int(num) > 100 else int(num) for num in num_list]

# print(num_list)
#
# ⬇️Exercise 2 --- 7
# def add_daily_temp(temp_dict, temp, day):
#     if day not in temp_dict:
#         temp_dict[day] = temp
#     return temp_dict


# temp_dict = {}

# temp_dict = add_daily_temp(temp_dict, 20, 'Monday')
# temp_dict = add_daily_temp(temp_dict, 25, 'Tuesday')
# temp_dict = add_daily_temp(temp_dict, 22, 'Wednesday')
# temp_dict = add_daily_temp(temp_dict, 23, 'Thursday')
# temp_dict = add_daily_temp(temp_dict, 24, 'Friday')

# temp_dict = add_daily_temp(temp_dict, 30, 'Tuesday')

# print(temp_dict)


# ⬇️Exercise 2 --- 8
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# result_dict = {}
# result_dict.update(dic1)
# result_dict.update(dic2)
# result_dict.update(dic3)

# print(result_dict)


# ⬇️Exercise 2 --- 9
# sample_data = {'item1': 45.50, 'item2': 35,
#                'item3': 41.30, 'item4': 55, 'item5': 24}

# top1, top2, top3 = '', '', ''

# for item in sample_data:
#     if sample_data[item] > sample_data.get(top1, 0):
#         top3, top2, top1 = top2, top1, item
#     elif sample_data[item] > sample_data.get(top2, 0):
#         top3, top2 = top2, item
#     elif sample_data[item] > sample_data.get(top3, 0):
#         top3 = item

# print(
#     f"{top1}: {sample_data[top1]}, {top2}: {sample_data[top2]}, {top3}: {sample_data[top3]}")

# ⬇️Exercise 2 --- 10
# students = [
#     {"student_id": 1, "name": "Dipesh Bhattarai", "class": "V"},
#     {'student_id': 2, 'name': 'Sujan Aryal', 'class': 'V'},
#     {'student_id': 3, 'name': 'Sajan Mainali', 'class': 'VI'},
#     {'student_id': 4, 'name': 'Iron Man', 'class': 'VI'},
#     {'student_id': 5, 'name': 'Peter Parker', 'class': 'VII'}
# ]

# key = 'name'
# value = 'Dipesh Bhattarai'

# if any(d.get(key) == value for d in students):
#     print(f"Key: '{key}' and Value: '{value}' do exist")
# else:
#     print(f"Key: '{key}' and Value: '{value}' do not exist")

# key = 'address'
# value = 'Superman'

# if any(d.get(key) == value for d in students):
#     print(f"Key: '{key}' and Value: '{value}' do exist")
# else:
#     print(f"Key: '{key}' and Value: '{value}' do not exist")


# ⬇️Exercise 3 --- 1
# def strings_with_a(list):
#     return [s for s in list if 'a' in s]


# my_list = ['apple', 'banana', 'Dipesh', 'Bhattarai']
# result_list = strings_with_a(my_list)
# print(result_list)

# ⬇️Exercise 3 --- 2
# ⬇️Simple way
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# common_elements = {x for x in set1 if x in set2}

# print(common_elements)

# ⬇️ Other way using & example for exercise 3---1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# common_elements = set1 & set2
# print(common_elements)

# ⬇️ Other way .intersection() example for exercise 3---1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# common_elements = set1.intersection(set2)

# print(common_elements)


# ⬇️Exercise 3 --- 3
# people = [
#     {"name": "Dipesh", "age": 17},
#     {"name": "Tony", "age": 10},
#     {"name": "Hulk", "age": 80},
#     {"name": "Thor", "age": 1500}
# ]

# over_18 = [person for person in people if person["age"] > 18]

# print(over_18)


# ⬇️Exercise 3 --- 4
# strings = {"Dipesh", "Bhattarai", "apple", "banana"}

# vowel_strings = {st_r for st_r in strings if st_r[3] in "aeiouAEIOU"}

# print(vowel_strings)


# ⬇️Exercise 3 --- 5
# num_list = [11, 33, 50]
# num_str = ""

# for num in num_list:
#     num_str = num_str + str(num)

# num_int = int(num_str)

# print(num_int)


# ⬇️Exercise 3 --- 6
# def get_weekend_average_temp(temp_dict):
#     weekend_days = ["Saturday", "Sunday"]
#     weekend_temps = []
#     for day, temp in temp_dict.items():
#         if day in weekend_days:
#             weekend_temps.append(temp)
#     if len(weekend_temps) == 0:
#         return 0
#     else:
#         return sum(weekend_temps) / len(weekend_temps)


# daily_temps = {
#     "Monday": 25,
#     "Tuesday": 28,
#     "Wednesday": 30,
#     "Thursday": 29,
#     "Friday": 26,
#     "Saturday": 22,
#     "Sunday": 23
# }
# weekend_avg = get_weekend_average_temp(daily_temps)
# print("Average temperature over the weekend:", weekend_avg)


# ⬇️Exercise 3 --- 7
# students = [
#     {"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
#     {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
#     {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
#     {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
#     {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}
# ]

# for student in students:
#     grades_sum = sum(student["grades"])
#     grades_len = len(student["grades"])
#     avg_grade = grades_sum / grades_len
#     print(student["name"] + ": " + str(avg_grade))


# ⬇️Exercise 3 --- 8
# books = [("The Jungle Book", "Dipesh Bhattarai"),
#          ("Rich Dad Poor Dad", "Steve Rogers"),
#          ("1984", "Doctor Banner"),
#          ("Brave New World", "Tony Stark")]

# # to store author name
# authors = []

# for book in books:
#     authors.append(book[1])

# authors.sort()

# sorted_books = []
# for author in authors:
#     for book in books:
#         if book[1] == author:
#             sorted_books.append(book)

# print(sorted_books)


# ⬇️Exercise 3 --- 9
# sample_list = [1, 2, 3, 4]
# # 'emp' used to specify the string that we want to insert at the beginning of each item in the original list.
# given_string = 'Dips'

# new_list = []
# for item in sample_list:
#     new_item = given_string + str(item)
#     new_list.append(new_item)

# print(new_list)


# ⬇️Exercise 3 --- 10
# color1 = ["white", "orange", "red", "green", "blue"]
# color2 = ["black", "yellow", "green", "blue"]

# diff_1 = list(set(color1) - set(color2))
# diff_2 = list(set(color2) - set(color1))

# print("Color1-Color2:", diff_1)
# print("Color2-Color1:", diff_2)


# ⬇️Exercise 1 --- 2
# import array
# my_array = array.array('i', [1, 2, 3, 4, 5])
# my_list = [1, "two", 3.0, ["four", 5]]
# print(my_array[2])
# print(my_list[1])


# ⬇️Exercise 1 --- 5
# Define a list of dictionaries representing people and their attributes
# people = [
#     {"name": "Dipesh", "age": 25},
#     {"name": "Superman", "age": 30},
#     {"name": "Thor", "age": 35},
# ]

# print(people[1]["name"])
# products = {
#     "fruits": ["apple", "banana", "mango"],
#     "prices": [1.0, 0.5, 1.5],
# }

# print(products["fruits"][2], products["prices"][2])


# ⬇️Exercise 4 --- 10
# ⬇️Exercise 4 --- 10
# ⬇️Exercise 4 --- 10
# ⬇️Exercise 4 --- 10
# ⬇️Exercise 4 --- 10
# ⬇️Exercise 4 --- 10
