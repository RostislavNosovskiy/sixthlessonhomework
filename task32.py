# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint 
listlen = int(input("Введите длинну списка:"))
list = [randint(-100,100) for i in range(listlen)]
minvalue = int(input("Введите минимальное значение диапазона:"))
maxvalue = int(input("Введите максимальное значение диапазона:"))
indexelementofrange = []
for i in range (listlen):
    if list[i]>=minvalue and list[i]<=maxvalue:
        indexelementofrange.append(i)
print(list)
print(indexelementofrange)