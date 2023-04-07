# # =========================== ⬇️ Labreport 6 ⬇️ ===========================
# Qeustion 1⬇️ Solution
# my_list = ["Dipesh", "Bhattarai", "Superman"]
# print("My list:", my_list)
# my_list.remove("Bhattarai")
# print("My list after removing Bhattarai:", my_list)
# my_list.append("Thanos")
# print("My list after adding 'Thanos':", my_list)
# my_list.extend(["Ironman", "Spiderman"])
# print("My list after adding 'Ironman' and 'Spiderman':", my_list)

# Qeustion 2⬇️ Solution
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)
# # Alternatively, merge the two dictionaries using the ** operator
# # merged_dict = {**dict1, **dict2}
# # print(merged_dict)


# Qeustion 3⬇️ Solution
# cars = [['Tesla', 'Model 5', 2021, 25000],
#         ['Lambo', 'Model S', 2022, 22000],
#         ['Ferrari', 'Model T', 2020, 35000],
#         ['Buggati', 'Model D', 2023, 80000]
#         ]
# print(cars)

# Qeustion 4⬇️ Solution
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = ("Dips", "Superman", "Thor")
# print("Before reversing tuple1:", tuple1)
# print("Before reversing tuple2:", tuple2)
# tuple1 = tuple1[::-1]
# tuple2 = tuple2[::-1]
# print("After reversing tuple1:", tuple1)
# print("After reversing tuple2:", tuple2)
# index = tuple2.index("Superman")
# print("The index of 'Superman' in tuple2 is:", index)


# Qeustion 5⬇️ Solution
# my_dict = {'apple': '3', 'banana': '5', 'cherry': '2'}
# for item in my_dict:
#     print(item + ": " + my_dict[item])
# sum_dict = {}
# for item in my_dict:
#     sum_dict[item] = int(my_dict[item])
# print(sum_dict)


# Qeustion 6⬇️ Solution
# set1 = {"Dipesh", "Banner", "Tony", "Thor"}
# set2 = {"Thor", "Loki", "Ironman", "Dipesh"}

# union_set = set1.union(set2)
# print("Union of sets:", union_set)

# intersection_set = set1.intersection(set2)
# print("Intersection of sets:", intersection_set)

# diff_set = set1.difference(set2)
# print("Difference of set1 - set2:", diff_set)

# diff_set = set2.difference(set1)
# print("Difference of set2 - set1:", diff_set)
