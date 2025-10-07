from math import floor, ceil

def closest_integer(value) -> int:
    if value.count('.') == 1:
        while len(value) > 0 and value[-1] == '0':
            value = value[:-1]
    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = round(num)
        res = int(res)
    else:
        res = 0
    return res