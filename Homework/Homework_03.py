import math

def sum_odd_index(list):
    result = 0
    for i in range(len(list)):
        if i%2 == 1:
            print(list[i], end = ', ')
            result += list[i]
    return result

def multiply_ends(list):
    new_list = []
    j = len(list)-1
    for i in range(math.ceil((len(list))/2)):
        new_list.append(list[i]*list[j])
        j -= 1
    return new_list

def get_fraction(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(round((float(list[i]))%1, 3))
    return(new_list)

def min_max_difference(list):
    min = list[0]
    max = list[0]
    for i in range(1, len(list)-1):
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]
    print('Minimum fractional part is:', min)
    print('Maximum fractional part is:', max)
    return round(max - min, 3)

def convert_2_bin(dec:int):
    bin = 0
    rank = 1
    remainder = 0
    dec = int(dec)
    while(dec > 0):
        remainder = int(dec%2)
        bin = bin + remainder*rank
        rank = rank*10
        dec = dec//2
    return bin

def fib(n):
    positive_list = [0, 1]
    for i in range(1, n):
        positive_list.append(positive_list[-1] + positive_list[-2])
    return positive_list

def negafib(n):
    negative_list = [0, 1]
    for i in range(1, n):
        negative_list.append(negative_list[-2] - negative_list[-1])
    return negative_list

# 1 - Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# my_list = [2, 3, 5, 9, 3]
my_list = [1, 5, 24, -72, 2, 0]
print(f'sum of elements with odd indexes = {sum_odd_index(my_list)}')


# 2 - Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_lst =  [2, 3, 5, 6]   
my_lst = [2, 3, 4, 5, 6]
print(my_lst, '=>', end = ' ')
print(multiply_ends(my_lst))

# 3 - Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564
     

my_list = [1.1, 1.2, 3.1, 5.567, 10.003]
print(f'Difference between min and max fractional parts is: {min_max_difference(get_fraction(my_list))}')


# 4 - Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = input('Enter number: ')
number = number.replace('-', '')
number = int(number)
print(f'The binary is: {convert_2_bin(number)}')


# 5 - Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/sH87m)


number = input('Enter number: ')
number = number.replace('-', '')
number = int(number)
final_list = negafib(number)[::-1] + fib(number)[1:]
print(final_list)