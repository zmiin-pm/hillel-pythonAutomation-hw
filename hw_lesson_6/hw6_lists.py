"""Function for user input"""


def user_input(num_of_args, arg_type, message):
    list_from_user = []
    for _ in range(num_of_args):
        list_from_user.append(
            arg_type(input(message))
        )
    return list_from_user


"""Задание 1:
Запросить у пользователя 5 чисел и записать их в список
"""
print('Please input 5 numbers ')
list_of_five = user_input(5, int, 'number: ')
print(f'Your list is: {list_of_five}')


"""Задание 2:
Дан список A = [1, 2, 3, 4, 5]
Удалить последнее число из списка
"""
last_number = list_of_five.pop()
print(f'Last number "{last_number}" was deleted from list\nNow list is: {list_of_five}')

"""Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""
print('Please input 10 numbers ')
list_of_ten = user_input(10, int, 'number: ')
nuber_to_find = int(input('Input number to find in list: '))
print(
    f'"{nuber_to_find}" occurs in list {list_of_ten} for {list_of_ten.count(nuber_to_find)} time(s)'
)

"""Задание 4:
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""
list_len = int(input('Please input number: '))
list_of_N = user_input(list_len, int, f'Input {list_len} numbers: ')
list_of_N.reverse()
print(f'Reversed list:', list_of_N)

"""Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""
list_of_five_to_compare = user_input(5, int, 'Input 5 numbers: ')
list_more_than_5 = [x for x in list_of_five_to_compare if x > 5]
print(f'List of numbers which are more than "5" is {list_more_than_5}')

"""Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла
(запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
"""
list_len = int(input('Please input number: '))
list_of_N = user_input(list_len, int, f'Input {list_len} numbers: ')
max_val, min_val = list_of_N[0], list_of_N[0]
for i in list_of_N:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
print(f'Max value: {max_val}\nMin value: {min_val}')

"""
Задание 7:
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3
"""
import re
text = user_input(1, str, "Input text with numbers: ")[0]
nums = re.findall(r'\d+', text)  # using regexp
print(f'Количество чисел: {len(nums)} {nums} using regexp')

numbers = []  # using loops
counter = 0
while counter <= len(text) - 1:
    if text[counter].isalpha():
        counter += 1
        continue
    else:
        number = ''
        while counter <= len(text) - 1 and text[counter].isdigit():
            number += str(text[counter])
            counter += 1
        numbers.append(number)

print(f'Количество чисел: {len(numbers)} {numbers} using loops')
