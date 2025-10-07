from math import floor, ceil

def closest_integer(value):
    dot_count = value.count('.')
    if dot_count == 1:
        while value.endswith('0'):
            value = value[:-1]
    num = float(value)
    last_two_chars = value[-2:] if len(value) >= 2 else ''
    if last_two_chars == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    else:
        res = int(round(num)) if len(value) > 0 else 0
    return res