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

##Кортежи - это неизменный список

#t = () # создание пустого  кортежа
#print(type(t)) #class <'tuple'>

#t = (1,)
#print(type(t))

#t = (1)
#print(type(t))# class int

t = (1, 2, 3) 
print(type(t)) # class tuple


#список преобразуем в кортеж
"""
v = [1, 2, 3]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b, c = v
print(a, b, c)
"""
t = (1, 2, 3,)
print(t[1]) # кортеж можно выводить по элементам
















