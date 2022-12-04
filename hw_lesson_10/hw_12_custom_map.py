from typing import Iterable, Callable


def custom_map(function: Callable, *iterables: Iterable) -> Iterable:
    return [function(iterable) for iterable in zip(*iterables)]

print(
    custom_map(sum, [1, 2, 3], [3, 5, 0, 5])
)
print(
    custom_map(max, [1, 5, 3], [2, 4, 6])
)
