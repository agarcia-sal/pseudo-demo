from math import floor, ceil

def closest_integer(value):
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]
    num = float(value)
    if value[-2:] == '.5':
        res = ceil(num) if num > 0 else floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0
    return res