# from typing import List

# # можно прописать тип данных (List), тогда type hint работает
# def sum_list(nums: List[int]) -> int:
#     '''
#     "doc string" в идеале пишется на англ
#     высчитывает сумму элементов списка

#     :param nums: список, состоящий из чисел
#     :return: сумма элементов списка
#     '''
#     return sum(nums)

# способ из лекции
# with open('text.txt') as data:

# способ рекомендованный на семинаре
# with open('text.txt') as file: 
#     data = file.read()
#     #readline, readlines
#     # for line in file.read() # в цикле надо не просто файл, а который мы читаем
#     for line in data: # или так, в перем data записано file.read()
#         print(line)


# 1. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# my_lst = ['38', 'fgdhg', 'jfdjh', 'hfhhr', '38', 'gkhr', 'jglj', '38']
# look_for = str(38)
# counter = 0
# for i in range(0, len(my_lst)):
#     if my_lst[i] == look_for:
#         counter += 1
        
#         if counter == 2:
#             print('index of second match is: ', i)
#     else:
#         continue
# if counter == 0:
#     print('not found')
# else:
#     print('number is found: ', my_lst[i], ', ', counter, 'x')

   

# 2. Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.

# ↑↑↑ немного добавила к первому решению

def findSecondIndex(list, word):
    n = 0
    for idx,item in enumerate(list):
        if (word == item):
            n += 1
        if (n == 2):
            return f'result = {idx}'
        return 'result - not found'

list_of_words = ['green', 'red', 'blue', 'yellow', 'green']
t = input('введите слово для поиска: ')
print(findSecondIndex(list_of_words, t))

# вариант из чата №2

lst = ['21','1', 'er', '21']
find_number = 1
#count = 2#количество вхождений
def find_nuber_in_list(lst_to_seek:list,number:int,count:int = 2):
    for i in range(0,len(lst_to_seek)):
        if lst_to_seek[i] == str(number):
            count = count-1
        if count == 0:
            return i
    return -1
pos_number = find_nuber_in_list(lst,find_number)
if pos_number != -1:
    print(pos_number)
else:
    print('в списке нет 2 вхождение')

# 3. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число