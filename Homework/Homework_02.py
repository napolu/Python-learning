# 1 - Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Enter number: ')

number = number.replace('-', '')
number = number.replace('.', '')
number = number.replace(',', '')

if not number.isdigit():
    print('Incorrect symbol')
else:
    number = int(number)
    sum = 0
    while number > 0:
        sum += number%10
        number //= 10
        print(sum)
    print('Final sum is: ', sum)
    


# 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = input('Enter number: ')

if not number.isdigit():
    print('Incorrect symbol')
else:
    number = int(number)
    factrl = 1
    for i in range(1, number+1):
        factrl = factrl * i
        print(factrl, end = ' ')



# 3 - Задайте список из n чисел последовательности (1+1/n)**n 
# и выведите на экран их сумму.

# Пример:
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

num = input('Enter number: ')

if not num.isdigit():
    print('Incorrect symbol')
else:
    num = int(num)
    dict = {}
    for i in range(1, num+1):
        dict[i] = (1+1/i)**i
    print(dict)



# 4 - Реализуйте выдачу случайного числа 
# (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time 
# (миллисекунды или наносекунды) - для задания случайности

import time
numOrig = time.time_ns()
print(numOrig)
num = str(numOrig)
#size = int(input('Enter digit capacity of number: '))
size = int(num[9])+1
polarity = int(num[10])
num = num[9:9 + size]

if polarity % 2 == 0:
    num = int(num)
else:
    num = -int(num)

print(num)
