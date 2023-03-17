"""
##Урок 2. Коллекции данных. Профилирование и отладка

#списки

#list_1 = []
#или 
#list_1 = list()

list_1 = [1, 2, 5, 8]
print(list_1)
print(*list_1) # (*) убирает скобки и запятые

"""

"""
#использование в цикле for

list_1 = [1, 2, 3, 6]
#for i in list_1:
#    print(i, end= " ")

print(len(list_1)) # выводит кол-во эл-тов

print(list_1[-1]) # можем выводить по элиментам

list_1.append(11) # добавляет элемент
print(list_1)

list_1.pop() # удаление последнего элемента
print(list_1)

list_1.pop(2) # удаление конкретного элимента
print(list_1)

list_1.insert(2, 15) # добовляет элемент на нужную позицию
print(list_1)

"""
"""
##Кортежи - это неизменный список

#t = () # создание пустого  кортежа
#print(type(t)) #class <'tuple'>

#t = (1,)
#print(type(t))

#t = (1)
#print(type(t))# class int

#t = (1, 2, 3) 
#print(type(t)) # class tuple


#список преобразуем в кортеж

v = [1, 2, 3]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b, c = v
print(a, b, c)

#t = (1, 2, 3,)
#print(t[1]) # кортеж можно выводить по элементам


t = (1, 2, 3, 4, 5)
#for i in t:
#    print(i)

for i in range(len(t)):
    print(t[i])
"""

###СЛОВАРИ - неупорядоченные коллекции произвольных объектов с доступом по ключу
"""
t = {} # {} - указывает что мы создали словарь
d = dict()# или так создать словарь

d['q'] = 'qwerty'
print(d)
d['w'] = 'werty'
print(d)
print(d['q'])
"""
"""
d ={}
d = {'r': 'rt', 'z': 'zs'}
del d['r'] # удаление элимента
print(d)
"""
"""
d ={}
d = {'r': 'rt', 'z': 'zs'}
print(d.items())
for item in d:
    print('{}:{}'.format(item, d[item]))

for (k,v) in d.items():
    print(k, v)

"""
###МНОЖЕСТВА содержат в себе уникальные элементы, не обязательно упорядочные
"""
colors ={'red', 'green', 'blue'}
print(colors)
colors.add('red')# можно добовлять
colors.add('grey')
colors.remove('red')# удалять
print(colors)
colors.discard('red')# усли эл-т есть то удаляет
colors.clear() #очищает множество
print(colors) # set{}

"""
"""
# Операции со множествами
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5} пересечение
dl = a.difference(b) # dl = {1, 3} разность
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
"""

#замороженное множество не можем его изменять
"""
a = {1, 8, 6}
b = frozenset(a)
print(b)
"""
#  генератор списков
list_1 = [i for i in range(1, 101)] 
# or(или)
list_1 = []
for i in range(1, 101):
    list_1.append(i)

list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6, ... , 100] # только четные числа
# также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)# [0, 4, 8, 12, 16]

# допустим, вы решили содать пары каждому из чисел(кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]









