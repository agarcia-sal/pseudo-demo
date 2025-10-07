from math import floor, ceil

def closest_integer(value):
    if '.' in value:
        while value[-1] == '0':
            value = value[:-1]

    num = float(value)

    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0

    return res