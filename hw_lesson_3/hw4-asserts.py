"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
"""
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
first_check = a > 10 and b > 10 and c > 10
second_check = (a % 3 == 0) and (b % 3 == 0)
print('Yes') if (first_check and second_check) else print('no')
"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c. 
Найдите наибольшее число из них и запишите в переменную max.
"""
max = max(a, b, c)
print(max)
"""
Пользователь вводит два числа A и B, 
нужно вывести сумму всех четных чисел в диапазоне от A до B.
"""
sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        sum += i
print(sum)