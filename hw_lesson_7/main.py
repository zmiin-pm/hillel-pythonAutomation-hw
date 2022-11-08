import re
import random
import collections

def find_nums_in_file(path):
    """
    Задание 1
    Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
    """
    with open(path) as f:
        text = f.read()
        return re.findall(r'\d+', text)


def write_user_text_to_file(path):
    """
    Задание 2
    Запросить у пользователя текст и записать его в файл data.txt
    """
    user_text = input(f'Input text to write to file {path}: ')
    with open(path, 'w') as f:
        f.write(user_text)
    return f'The text was successfully written to {path}'


def write_user_numbers_to_file(path):
    """
    Задание 3
    Запросить у пользователя число N и запросить N чисел у пользователя,
    потом записать их в файл numbers.txt через пробел
    """
    num_of_num = int(input(f'Input number: '))
    user_numbers = []
    for i in range(num_of_num):
        user_numbers.append(
            input(f'Input {num_of_num - i} numbers: ')
        )
    with open(path, 'w') as f:
        f.write(' '.join(user_numbers))
    return f'Numbers were successfully written to {path}'


def gen_random_numbers_to_file(path):
    """
    Задание 4
    Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
    """
    with open(path, 'w') as f:
        random_numbers = [random.randint(0, 100) for _ in range(100)]
        f.writelines(
            list(map(lambda x: str(x) + '\n', random_numbers))
        )
    return f'Random numbers were successfully written to {path}'


def count_words_in_file(path):
    """
    Задание 5
    Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
    """
    with open(path) as f:
        text = f.read()
        words = re.findall(r'[a-zA-Z]+', text)
        return len(words)


def sum_of_numbers(path):
    """
    Задание 6
    Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
    """
    with open(path) as f:
        numbers = f.read().split(' ')
        return sum(list(map(int, numbers)))


def top_of_words(path):
    """
    Задание 7
    Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются,
    """
    with open(path) as f:
        text = f.read()
        words = re.findall(r'[a-zA-Z]+', text)
        counter = collections.Counter(words)
        list_of_tuples = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        return list_of_tuples[:5]

#
# print(find_nums_in_file.__doc__)
# file_path = './src/text.txt'
# numbers = find_nums_in_file(file_path)
# print(f'Numbers from file {file_path}:  {numbers}')
#
# print(write_user_text_to_file.__doc__)
# file_path_2 = './src/user_text.txt'
# print(write_user_text_to_file(file_path_2))
#
# print(write_user_numbers_to_file.__doc__)
# file_path_3 = './src/numbers.txt'
# print(write_user_numbers_to_file(file_path_3))
#
# print(gen_random_numbers_to_file.__doc__)
# file_path_4 = './src/random_numbers.txt'
# print(gen_random_numbers_to_file(file_path_4))
#
# print(count_words_in_file.__doc__)
# file_path_5 = './src/text.txt'
# print(f'There are {count_words_in_file(file_path_5)} words in {file_path_5}')
#
# print(sum_of_numbers.__doc__)
# file_path_6 = './src/numbers.txt'
# print(f'Sum of numbers in {file_path_6} is: {sum_of_numbers(file_path_6)}')

print(top_of_words.__doc__)
file_path_7 = './src/text.txt'
top_five = top_of_words(file_path_7)
for top_item in top_five:
    print(f'{top_item[0]} - {top_item[1]} раз')
