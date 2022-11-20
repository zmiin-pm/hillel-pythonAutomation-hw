def change(lst):
    """
    1. Напишите функцию change(lst), которая принимает список
    и меняет местами его первый и последний элемент.
    В исходном списке минимум 2 элемента.
    """
    changed_lst = lst.copy()
    changed_lst[0] = lst[len(lst) - 1]
    changed_lst[len(changed_lst) - 1] = lst[0]
    return changed_lst


def to_dict(lst):
    """
    2. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
    в котором каждый элемент списка является и ключом и значением.
    Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
    """
    result_dict = dict(zip(lst, lst))
    return result_dict


def sum_range(start, end):
    """
    3. Напишите функцию sum_range(start, end),
    которая суммирует все целые числа от значения «start» до величины «end» включительно.
    Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
    """
    if end < start:
        start, end = end, start
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


def read_last(lines, file):
    """
    4. Напишите функцию read_last(lines, file),
    которая будет открывать определенный файл file и выводить на печать построчно последние строки
    в количестве lines (на всякий случай проверим, что задано положительное целое число).
    """
    if lines < 0:
        raise AttributeError('Please enter positive number')
    with open(file) as f:
        lines_from_file = f.readlines()
        lines_from_file.reverse()
        lines_from_file = list(map(lambda x: x.replace('\n', ''), lines_from_file))
    return lines_from_file[:lines]

user_list = ['2', '1', 'apple']

print(change.__doc__)
print(f'input: {user_list}')
print(change(user_list))

print(to_dict.__doc__)
print(f'input: {user_list}')
print(to_dict(user_list))

print(sum_range.__doc__)
start_val, end_val = 1, 10
print(f'input: {start_val}, {end_val}')
print(sum_range(start_val, end_val))

print(read_last.__doc__)
file_path = '../hw_lesson_7/src/text.txt'
last_lines = 3
print(f'{last_lines} last lines from file ({file_path}):')
lines_file = read_last(last_lines, file_path)
for line in lines_file:
    print(line)




