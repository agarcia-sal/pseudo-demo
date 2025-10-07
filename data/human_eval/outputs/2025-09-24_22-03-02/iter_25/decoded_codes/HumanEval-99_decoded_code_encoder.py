def closest_integer(value: str) -> int:
    from math import floor, ceil
    count_dot = 0
    for index in range(len(value)):
        if value[index] == '.':
            count_dot += 1
    if count_dot == 1:
        while len(value) > 0 and value[-1] == '0':
            value = value[:-1]
    num = float(value)
    length_value = len(value)
    if length_value >= 2 and value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif length_value > 0:
        rounded_num = round(num)
        res = int(rounded_num)
    else:
        res = 0
    return res