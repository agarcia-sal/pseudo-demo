from math import floor, ceil

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value[-1] == '0':
            value = value[:-1]
    num = float(value)
    if value[-2:] == '.5':
        res = ceil(num) if num > 0 else floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0
    return res