from math import floor, ceil

def closest_integer(value: str) -> int:
    dot_count = value.count('.')
    if dot_count == 1:
        while True:
            last_index = len(value) - 1
            if last_index < 0:
                break
            last_char = value[last_index]
            if last_char == '0':
                value = value[:last_index]
            else:
                break
    try:
        num = float(value)
    except ValueError:
        return 0
    length_value = len(value)
    if length_value >= 2:
        last_two_chars = value[-2] + value[-1]
        if last_two_chars == '.5':
            if num > 0:
                res = ceil(num)
            else:
                res = floor(num)
        else:
            if length_value > 0:
                rounded_num = round(num)
                res = int(rounded_num)
            else:
                res = 0
    else:
        if length_value > 0:
            rounded_num = round(num)
            res = int(rounded_num)
        else:
            res = 0
    return res