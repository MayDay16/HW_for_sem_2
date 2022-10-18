
# # Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# # N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# i = 1
# j = 1
# N = int(input('Введите число N '))
# while j<=N:
#     i = i*j
#     j += 1
#     print (i)

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

# print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             print(f"{x} | {y} | {z} | {int(not(x and y) or z)}") 

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

# str1 = input(str('введите строку №1 '))
# str2 = input(str('введите строку №2 '))
# str3 = None
# str1 = str1.lower ()
# str2 = str2.lower ()

# list = []
# for i in range(len(str1)):
#     count = 0
#     for z in range(len(str2)):
#         if str1[i] == str2[z]:
#             count += 1
#     str3 = f"{str1[i]} - {count}"
#     list.append(str3)
# print()
# print('Количество повторов символов первой строки во второй строке:' )
# print()
# print(list)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

# N = int(input('Введите число N: '))
# shift = 2
# list = [*range(-N, N+1)]
# print([*list[len(list)-shift:], *list[:len(list)-shift]])