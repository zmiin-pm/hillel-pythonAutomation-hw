"""
Задание 1:
Пользователь вводит слово, если это слово является полиндромом,
то вывести '+', иначе '-'
"""

word = input('Please input a palindrome (register isn\'t important): ')
word = word.lower()
word = word.strip()
print('+') if word == word[::-1] else print('-')

"""
Задание 2:
Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'
"""

text = input('Please input some text: ')
word_to_find = input('Please input a word to find (register is important): ')
print('YES') if text.find(word_to_find) != -1 else print('NO')


"""
Задание 3:
Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.
"""

string = input('Please input a string (register is important): ')
if string.startswith('abc'):
    string = 'www' + string[3:]
else:
    string = string + 'zzz'
print(string)

"""
Задание 4:
Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
"""

string_to_remove_digits = input('Please input a string with digits: ')
import re

print(
    re.sub('(\d+)', '', string_to_remove_digits)
)

string_without_digits = ''
for i in string_to_remove_digits:
    if not i.isdigit():
        string_without_digits += i

print(string_without_digits)

"""
Задание 5:
Написать валидатор для почты. 
Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.', 
и если это так, то вывести "YES", иначе "NO"
"""

email_string = input('Please input an email: ')
if not re.match('(.+@.+\..+)', email_string):
    print('email validated: NO')
else:
    print('email validated: YES')
