 # УПРАВЛ КОНСТРУКЦИИ IF, IF-ELSE
# if condition:
  # operator 1
  # operator 2
  # ...
  # operator n
# else:
  # operator n+1
  # operator n+2
  # etc

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)


# if condition:
  # operator
# elif condition:
  # operator
# elif condition:
  # operator
# else:
  # operator


# УПРАВЛ КОНСТРУКЦИЯ WHILE
# while condition:
  # operator 1
  # operator 2
  # ...
  # operator n

original = 235 # реверс числа
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# WHILE-ELSE
# ну то же самое как в if-else

original = 872 # реверс числа
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    #print(original) # можно вывести число на каждом этапе
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

# УПРАВЛ КОНСТРУКЦИИ FOR
# for i in enumeration:
  # operator 1
  # operator 2
  # ...
  # operator n

for i in 1,2,3,4,5:
    print(i**2) # квадраты чисел

list = [4,5,6,7,8] # вариант со списком
for i in list:
    print(i**2)

r = range(10) # рейндж (0 - 9)
for i in r:
    print(i) 

#вариант
for i in range (1, 5): # числа от 1 до 4
    print(i)

for i in range (1, 10, 2): # числа 1-9, третьим аргументом приращение
    print(i)

for i in 'qwerty': # в к-ве итерируемого объекта могут выступать и строки
    print(i)


#СТРОКИ
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39 - длина текста
print('ещё' in text) # True проверка на наличие к-то подстроки в тексте
print(text.isdigit()) # False проверка, явл-ся ли символи цифрами
print(text.islower()) # True проверка, явл-ся ли символы символами ниж регистра
print(text.replace('ещё', 'ЕЩЁ')) # заменить что-то

for c in text:
    print(c) # про это не пояснили, но было в презентации))


# СРЕЗЫ В СТРОКАХ
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # с
print(text[1]) # ъ
#print(text[len(text)]) # IndexError (считается с 0, тут индекс выходит за пределы текста)
print(text[len(text)-1]) # к (последний элемент)
print(text[-5]) # б (считается с конца)
print(text[:]) # символы от первого до посл, = print(text)
print(text[:2]) # символы от 0 до 1
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл (начало:конец:шаг)
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[2]


# СПИСКИ

numbers = [1, 2, 3, 4, 5]
print(numbers)

#numbers = list(range(1, 6)) # здесь тип рейндж приведён к типу лист
#print(numbers)

numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]


colours = ['red', 'green', 'blue']
for e in colours:
    print(e)  # red green blue

for e in colours:
    print(e*2)  # redred greengreen blueblue

colours.append('gray') # добавить в конец
print(colours == ['red', 'green', 'blue', 'gray']) # True
colours.remove('red') #del colours[0] # удалить элемент


# ФУНКЦИИ
#def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

def f(x):
    if x == 1:
        return 'Целое' # возвращается тип string
    elif x == 2.3:
        return 23 # возвращается тип int
    else:
        return # возвращается тип NoneType (ничего)

arg = 1
print(f(arg))