#python3 -m venv .folde  - создает виртуальное окружение
# int    - целые числа
# float  - дробные числа
# bool   - логический тип данных (True/False)
# str    - строка
# n = a  - создание переменной
# n = 'eftgy'
# n = 1.56
# print(n) - вывод переменной
# print(type(n)) - вывод функции тип


print(a,' - ', b, '-',c) или 
print(f"{a} - {b} - {c}") или
print("{} - {} - {}".format(a,b,c))

a = input() ввод
print(a)
b = input('введите втоорое число: ' )

print(a, ' + ', b, ' = ', a + b) #сложение

# перевод в целочисленное значение
с = 5.78
print(c)
n - int(c)
print(n)
    
a = int(input()) ввод
print(a)
b = int(input('введите втоорое число: ' ))
print(a, ' + ', b, ' = ', a + b)

Птиоритет арефметических операций:
1. Возведение в степень (**)
2. Умножение (*)
   a = 6.743838
   b = 8.54545
   print(a*b) чтобы оставить х знаков после запятой используем функцию round()
    print(round(a*b, 3))
3. Деление (/)
4. Целочисленное деление (//)
5. Остаток от деления (%)
6. сложение(+)
7. Вычитание(-)

логические операции
>       больше
>=      больше или равно
<       Меньше
<=      Меньше или равно
==      Равно
!=      не равно
not     не(отрицание)
and     и (конъюкция)
or      или (дизъюнкция)




управляющие конструкции: if, if-else
отступы  кнопка таб или 4 пробела
пример оформления:
if condition:
    # operator 1
    # operator 2
    # ...
    # operator n
else:
    # operator n + 1
    # operator n + 2
    # ...
    # operator n + m

еще один вариант
if condition1:
    # operator 
elif condition2:
     # operator
 else:
    #operstor

сложные условия
if condition1 and condition2:(оба условия верны)
    # operator
if condition or condition1:(одно из условий верно)
    # operator  

Цикл While 
while condition:             n = 423
    #operator 1              summa = 0
    #operator 2              while n > 0
      # .....                    x = n % 10
    #operator n                  summa    -
                             summa + x
                                 n = n // 10
                             print(summa)

While else, break
метод флага
пр.
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: если остаток пр деление числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1


Цикл for, функция range()
for i in enumeration:
    #operator1
    #operator2
    # ...
    #operator n

for i in 1, -2, 3, 14, 5:
    print(i)

range()
- выдает значение из диапазона с шагом 1.
- если указано только одно число - от 0 до задонного
- если нужен другой шаг, третьим аргументом можно задать приращение.
r = range(5) # 0 1 2 3 4
r = range(2, 5)# 2 3 4
r = range(0, -5)# ----
r = range(1, 10, 2)# 1 3 5 7
r = range(100, 0,-20)# 100 80 60 40 20

r = range(100, 0, -20)# range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20

можно использовать с строками 
for i in 'qwert':
    print(i)



    строка
функция len( позволяет узать размер строки)
print(len(text))
можно проверить если слово(что-то) в строке# print('что-то' in text)
функция lower(переводит в нижний регистр)
print(text.lower())
функция upper(переводит в верхний регистр)
print(text.upper())
функция replace() меняет в строке одно на другое
print(text.replace('что меняем', 'на что меняем'))

срезы
