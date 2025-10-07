from math import floor, ceil

def closest_integer(value):
    count_dot = value.count('.')
    if count_dot == 1:
        while value and value[-1] == '0':
            value = value[:-1]
    num = float(value)
    length_value = len(value)
    if length_value >= 2:
        substring_last_two = value[-2] + value[-1]
    else:
        substring_last_two = ''
    if substring_last_two == '.5':
        res = ceil(num) if num > 0 else floor(num)
    else:
        res = int(round(num)) if length_value > 0 else 0
    return res