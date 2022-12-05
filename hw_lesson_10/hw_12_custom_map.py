from typing import Iterable, Callable, List


def custom_map(function: Callable, *iterables: Iterable) -> List:
    """
    2. Написать функцию, которая возвращает список результатов выполнения заданной функции, к соответствующим элементам переданных итерируемых объектов.
    Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
    custom_map(sum, [1, 2, 3], [3, 5, 0, 5]) -> [4, 7, 3]
    """
    iterables = iterables[0] if len(iterables) == 1 else zip(*iterables)
    return [function(iterable) for iterable in iterables]


print(
    custom_map(sum, [1, 2, 3], [6, 7, 3])
)
print(
    custom_map(max, [1, 5, 3], [2, 4, 6])
)
print(
    custom_map(str, [17, 23])
)
