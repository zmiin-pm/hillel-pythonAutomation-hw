from typing import Iterable, List, Tuple
from copy import deepcopy

"""
3. Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
"""


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    inner_seq = deepcopy(sequences)
    if full:
        index = len(max(inner_seq, key=len))
        for sequence in inner_seq:
            while len(sequence) < index:
                sequence.append(default)
    else:
        index = len(min(inner_seq, key=len))
    return [tuple(map(lambda sequence: sequence[i], inner_seq)) for i in range(index)]


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq1, seq2, full=True) == [(1, 9), (2, 8), (3, 7), (4, None), (5, None)]
assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
