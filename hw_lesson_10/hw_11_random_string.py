from random import choice


def get_random_string(length: int) -> str:
    numbers = [chr(i) for i in range(48, 58)]
    big_letters = [chr(i) for i in range(65, 91)]
    small_letters = [chr(i) for i in range(97, 123)]
    all_signs = ''.join(numbers + big_letters + small_letters)
    return ''.join(choice(all_signs) for _ in range(length))


print(
    get_random_string(20)
)

def get_random_string_2(length: int) -> str:
    numbers = {chr(i) for i in range(48, 58)}
    big_letters = {chr(i) for i in range(65, 91)}
    small_letters = {chr(i) for i in range(97, 123)}
    numbers.update(big_letters, small_letters)
    return ''.join(numbers.pop() for _ in range(length))

print(
    get_random_string_2(20)
)