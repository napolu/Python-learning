# ФАЙЛЫ

# хранение данных, передача данных в клиент-серверных проектах, 
# хранение конфигов, логирование действий
# связать переменную с файлом, определив модификатор работы
# a - открытие для добавл данных
# r - открытие для чтения данных
# w - открытие для записи д-х (перезапись)
# w+, r+ миксованные режимы


# colours = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colours) # разделителей не будет
# data.write('\nLINE 2\n') 
# data.write('LINE 3\n')
# data.close()

# with open('file.txt', 'w') as data: # др способ
#     data.write('line 1\n')
#     data.write('line 2\n') # здесь закрытие файла автоматически делается


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()



# ФУНКЦИИ И МОДУЛИ

# import lec_01_pt2 as l # сократить название файла
# print(l.f(1))  # импорт функции из файла с первой лекцией 
# # (незакоменченный шмурдяк тож импортировался)

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!!
# print(new_string('!')) # TypeError missing 1 required

# def new_string(symbol, count = 3): # можно указать значение каунта по умолчанию
#     return symbol * count

# print(new_string(4)) # 12 теперь работает
# print(new_string('!')) # !!!



# ПЕРЕДАЧА НЕОГРАНИЧ КОЛ-ВА АРГУМЕНТОВ

# def concatenatio(*params): # перед аргументом ставится звёздочка 
#     # и далее с ним работа как с набором
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError здесь логика для строк



# РЕКУРСИЯ

# def fib(n): # Фибоначчи
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34



# КОРТЕЖИ (кортеж - неизменяемый список)

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# a, b = 3, 4 # обычное множественное присваивание
# a = (3, 4, 5) # внезапно оно превращается в кортеж
# # print(a)
# # print(a[0]) # можем обращаться к опр элементу
# # print(a[-1]) # по аналогии со строками посл элемент
# # # в списке можно присвоить новое значение элементу, в кортеже - нет
# # b = (3,) # кортеж из 1 элемента - нужна запятая

# for item in a:   # кортеж в цикле
#     print(item)


# t = tuple(['red', 'green', 'blue']) # создаём список, преобр его в кортеж
# red, green, blue = t    # кортеж распаковываем и превращаем в 3 независимых переменных
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue



# СЛОВАРИ
# неупорядоченные коллекции произв объектов с доступом по ключу

# dictionary = {}  # обратный слеш для того чтобы не писать всё в 1 строчку
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys(): # просмотр только самих ключей
#     print(k)

# for k in dictionary.values(): # просмотр значений
#     print(k)

# for k in dictionary.keys():
#     print(dictionary[k])

# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up']) #можно присвоить др значение

# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

# for item in dictionary: # for (k,v) in dictionary.items(): #вывод попарно
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# down: ↓
# right: →



# МНОЖЕСТВА
# Неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # добавление уже существующиго = ничего
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавление нового
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удаление элемента
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red' - т.к. удаление несуществующего
# colors.discard('red') # ok - удаление не приводящее к ошибке, если элемента нет
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } # очистить множество и получить пустое
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} множество на основе имеющегося
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}  объединение
# i = a.intersection(b) # i = {8, 2, 5}  пересечение
# dl = a.difference(b) # dl = {1, 3}  разность
# dr = b.difference(a) # dr = {13, 21}
 
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}  # неизменяемое множество
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})



# СПИСКИ (некоторое углубление)
list1 = [1, 2, 3, 4, 5]
list2 = list1 
# когда список копируется так, 
# то изменения происходят синхронно и в обоих списках

# for e in list1:
#     print(e)
# print()

# for e in list2:
#     print(e)
# print()

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)
# print()

# for e in list2:
#     print(e)
# print()

# извлекает последний элемент списка
# print(list1.pop()) 
# print(list1) 
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# удаление конкретного элемента - 
# # индекс элемента используем как аргумент в ф-ции pop
# print(list1.pop(2)) 
# print(list1)

# вставка элемента - на позицию с индексом 2 вставляется элемент "11"
print(list1.insert(2, 11)) 
print(list1)

# просто добавление в конец списка
print(list1.append(11))
print(list1)