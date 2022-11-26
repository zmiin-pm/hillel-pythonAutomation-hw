def is_power_of_two(num: int, power=1, counter=0):
    if power > num:
        return 'no'
    if power == num:
        return f'yes {counter}'
    return is_power_of_two(num, power*2, counter+1)


print(is_power_of_two(1048576))
