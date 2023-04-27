# ⬇️ 1
# def fact(n):
#     if n > 0:
#         return n * fact(n-1)
#     else:
#         return 1


# num = int(input("Enter a number: "))
# print(fact(num))

# ⬇️ 2
# def recursivefunc(n):
#     print('n = ', n)
#     if n > 0:
#         recursivefunc(n - 1)


# recursivefunc(4)

# ⬇️ 3
# def fact(n):
#     if n < 1:
#         return 1
#     else:
#         return n * fact(n-1)


# print(fact(4))

# ⬇️ 4
# def sum(n):
#     if len(n) == 0:
#         return 0
#     else:
#         print(n[1:])
#         return n[0] + sum(n[1:])


# add = [1, 2, 3, 4, 5, 6]
# print(sum(add))

# ⬇️ 5
# def ordered_find(c, abc):
#     start = 0
#     end = len(abc)-1
#     while start <= end:
#         mid = (start + end)//2
#         if c == abc[mid]:
#             return mid
#         if c < abc[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1


# abc = ['a', 'b', 'c', 'd', 'e']
# c = 'c'
# print(ordered_find(c, abc))


# ⬇️ 6
def reverse(list):
    if len(list) == 0:
        return []
    else:
        print(list[:-1])
        return [list[-1]] + reverse(list[:-1])


list = [1, 2, 3, 4, 5, 6]
print(reverse(list))
