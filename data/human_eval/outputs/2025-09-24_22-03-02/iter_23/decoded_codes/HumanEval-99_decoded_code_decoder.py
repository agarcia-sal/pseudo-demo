from math import floor, ceil

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while len(value) > 0 and value[-1] == '0':
            value = value[:-1]
    num = float(value)
    if len(value) >= 2 and value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0
    return res