from math import floor, ceil

def closest_integer(value: str) -> int:
    dot_count = value.count('.')
    if dot_count == 1:
        while len(value) > 0 and value[-1] == '0':
            value = value[:-1]
    num = float(value) if value else 0.0
    if len(value) >= 2:
        last_two_chars = value[-2] + value[-1]
    else:
        last_two_chars = ''
    if last_two_chars == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    else:
        res = int(round(num)) if len(value) > 0 else 0
    return res