import math

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0') and len(value) > 0:
            value = value[:-1]
    num = float(value) if len(value) > 0 else 0.0
    if len(value) >= 2 and value[-2:] == '.5':
        if num > 0:
            res = math.ceil(num)
        else:
            res = math.floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0
    return res