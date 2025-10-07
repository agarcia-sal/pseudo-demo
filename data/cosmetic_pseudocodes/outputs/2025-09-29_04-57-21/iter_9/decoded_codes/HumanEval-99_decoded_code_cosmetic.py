from math import ceil, floor


def closest_integer(value: str) -> int:
    if (value_contains_dot := '.' in value) and value.count('.') == 1:
        while value.endswith('0') and len(value) > 0:
            value = value[:-1]
    number = float(value)
    if value.endswith('.5'):
        if number > 0:
            output = ceil(number)
        else:
            output = floor(number)
    elif len(value) > 0:
        output = round(number)
    else:
        output = 0
    return output