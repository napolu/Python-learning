#СЛОВАРЬ
# week_days = {1:"Пн",2:"Вт",3:"Ср",4:"Чт",5:"Пт",6:"Сб",7:"Вс"}
# print(week_days.keys()) # ключи
# print(week_days.values()) # значения
# print(week_days.items()) # всё вместе
# print(week_days[3]) # конкретный ключ
# week_days['olga'] = 89650456534 # добавили элемент в словарь
# print(week_days)


# вариант проверки isdigit
# lst = list(range(1,8))
# while True:
#     number= input('введите цифру обозначающую день недели: ')
#     if not number.isdigit():
#         continue
#     elif number in lst:
#         break


#КРОСИВЕЙШЕЕ ТАБЛИЧКО из логической задачи (у меня немного смещается)
# print ('\nX \t Y \t Z \t ¬(X ⋁ Y ⋁ Z) \t ¬X ⋀ ¬Y ⋀ ¬Z \t ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \n')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             on_left = not(x or y or z)
#             on_right = not(x) and not(y) and not (z)
#             print(f'{x} \t {y} \t {z} \t {on_left} \t {on_right} \t {on_left == on_right}')



# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# n = int(input('Enter number: '))
# result = 1
# lst = [1]
# for i in range(n):
#     result *= -3
#     lst.append(result)
# print(lst)

#др вариант
# n = int(input('Enter number: '))
# result = 1
# for i in range(n):
#     print(result, end = ', ')
#     result *= -3
    

# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Enter number: '))
# dict = {}
# for i in range(1,n+1):
#     dict[i] = i*3 + 1
# print(dict)


# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.


string1 = input('Enter first string: ')
string2 = input('Enter second string: ')
if len(string1) < len(string2):
    string1, string2 = string2, string1
count = 0

for i in range(0, len(string1)-len(string2)+1): # если в "ко ко ко" считать "ко", то получается 2 :С
    if string2.lower() == string1[i:i+len(string2)].lower():
        count += 1
    # print(string1[i:i+len(string2)])
print(count)

# for i in string1:  #работает с 1 символом
#     if string2 == i:
#         count += 1
# print(count)

# for i in string1:
#     for j in string2:
#         if j in i:
#             count += 1
# print(count)


