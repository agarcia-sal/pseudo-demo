import math

def closest_integer(value):
    if '.' in value:
        value = value.rstrip('0')
        if value.endswith('.'):
            value = value[:-1]
    num = float(value)
    if value.endswith('.5'):
        res = math.ceil(num) if num > 0 else math.floor(num)
    else:
        res = round(num)
    return res