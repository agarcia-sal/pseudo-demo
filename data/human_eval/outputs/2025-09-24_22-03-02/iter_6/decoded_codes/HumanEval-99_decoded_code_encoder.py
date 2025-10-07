from math import floor, ceil

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]
    num = float(value)
    if value.endswith('.5'):
        if num > 0:
            result = ceil(num)
        else:
            result = floor(num)
    elif len(value) > 0:
        result = round(num)
    else:
        result = 0
    return result