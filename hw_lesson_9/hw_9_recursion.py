def is_power_of_two(num: int, power: int = 1, counter: int = 0) -> str:
    if power > num:
        return 'no'
    if power == num:
        return f'yes {counter}'
    return is_power_of_two(num, power*2, counter+1)


print(is_power_of_two(1048576))
