from copy import deepcopy
from typing import Iterable, Callable, List

def custom_map(function: Callable, *iterables: Iterable) -> List:
    """
    2. Написать функцию, которая возвращает список результатов выполнения заданной функции, к соответствующим элементам переданных итерируемых объектов.
    Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
    custom_map(sum, [1, 2, 3], [3, 5, 0, 5]) -> [4, 7, 3]
    """
    inner_iterables = deepcopy(iterables)
    inner_iterables = inner_iterables[0] if len(inner_iterables) == 1 else zip(*inner_iterables)
    if type(inner_iterables) == zip:
        return [function(*iterable) for iterable in inner_iterables]
    return [function(iterable) for iterable in inner_iterables]


sum2 = lambda x, y: x + y
sum3 = lambda x, y, z: x + y + z

assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
assert custom_map(str, (17, 23)) == ['17', '23']
assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
assert custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1]) == [5, 11, 9]
