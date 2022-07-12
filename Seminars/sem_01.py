# Задача 1. 
# Напишите программу, которая принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.

# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


# print('введите a');
# a = int(input())
# print('введите b');
# b = int(input())
# if a*a == b or b*b == a:
#     print('да')
# else:
#     print('нет')


# Задача 2. 
# Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.

# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


# print('введите a');
# a = int(input())

# print('введите b');
# b = int(input())

# print('введите c');
# c = int(input())

# print('введите d');
# d = int(input())

# print('введите e');
# e = int(input())

# numbers = [a, b, c, d, e]

# max_num = numbers[0]
# for item in numbers:
#     if max_num < item:
#         max_num = item
# print('maximum number is:', max_num)


# Задача 3.
# Пользователь вводит количество дней, 
# указывает процент скидки и вводит сумму. 
# Рассчитать прибыль, если за каждый день 
# сумма увеличивается на 3 $ и затем применяется скидка, 
# то есть итоговая сумма еще увеличивается 
# на данное число процентов.

# print('enter number of days:')
# days = int(input())
# print('enter discount %:')
# discount = int(input()) / 100
# print('enter sum, $')
# sum_dollars = int(input())
# sum_total = (sum_dollars + 3 * days) + (sum_dollars + 3 * days) * discount
# print('total: ', sum_total, '$')
# profit = sum_total - sum_dollars
# print('Your profit is ', profit, '$')

# Задача 4.
# Дано значение температуры в градусах Цельсия. 
# Вывести температуру в градусах Фаренгейта.

# print('Enter Celsium temperature:')
# temper_cels = int(input())
# temper_fahr = temper_cels * 1.8 + 32
# print('Fahrenheit temperature is ', temper_fahr)


# Задача 5.
# Пользователь вводит время в минутах и расстояние в километрах. 
# Найдите скорость в м/c.

# print('enter time, minutes: ')
# time_sec = float(input()) * 60
# print('enter distance, km: ')
# distance_m = float(input()) * 1000
# speed_m_sec = round(distance_m / time_sec, 1)
# print('speed is: ', speed_m_sec, 'm/sec')


# Задача 6.
# Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N

# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# print('введите n');
# n = int(input())
# lst = []
# for i in range(-n, n+1):
#     lst.append(i)
# print(lst)


# Задача 7.
# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

print('введите число');
a = float(input())
if a < 0:
    a = -a
result = int(a *10 % 10)
if result == 0:
    print('нет')
else:
    print(result)
