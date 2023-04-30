# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

from random import sample

n = int(input("Введите величину массива > "))
A = sample(range(1, 10), n)
print(A)

x = int(input("Введите число для поиска ближайшего значения > "))
minimum_difference = abs(A[0] - x)
nearest_value = [A[0]]
for i in range(1, n):
    diff = abs(A[i] - x)
    if diff < minimum_difference:
        minimum_difference = diff
        nearest_value = [A[i]]
    elif diff == minimum_difference:
        nearest_value.append(A[i])
print("Ближайшее число к", x, ":", nearest_value)


# n = int(input("Введите количество элементов в массиве: "))
# arr = []
# for i in range(n):
#     arr.append(int(input("Введите число: ")))
# x = int(input("Введите число для поиска: "))

# min_diff = abs(arr[0] - x)
# closest_num = arr[0]
# for i in range(1, n):
#     diff = abs(arr[i] - x)
#     if diff < min_diff:
#         min_diff = diff
# closest_num = arr[i]

# print("Ближайшее число к", x, ":", closest_num)
