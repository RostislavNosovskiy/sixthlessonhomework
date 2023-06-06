# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
firstElement = int(input("Введите первый член aрифметической прогрессии:"))
diffOfElement = int(input("Введите разность между смежными членами арифметической прогрессии:"))
countOfElement = int(input("Введите количество членов арифметической прогрессии:"))
ArithmeticProgression = []
for i in range (countOfElement):
    ArithmeticProgression.append(firstElement + i* diffOfElement)
print(*ArithmeticProgression)