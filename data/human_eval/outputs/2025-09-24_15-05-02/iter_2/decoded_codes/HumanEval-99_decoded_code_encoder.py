def closest_integer(value):
    from math import floor, ceil

    if '.' in value:
        while value.endswith('0'):
            value = value[:-1]

    num = float(value)

    if value.endswith('.5'):
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res