from typing import Iterable, List, Tuple

"""
3. Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
"""


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    if full:
        index = len(max(sequences, key=len))
        for sequence in sequences:
            while len(sequence) < index:
                sequence.append(default)
    else:
        index = len(min(sequences, key=len))
    return [tuple(map(lambda sequence: sequence[i], sequences)) for i in range(index)]


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
