from math import floor, ceil

def closest_integer(value) -> int:
    dot_count = 0
    i = 0
    while i < len(value):
        if value[i] == '.':
            dot_count += 1
        i += 1

    if dot_count == 1:
        while len(value) > 0:
            last_char_index = len(value) - 1
            if value[last_char_index] == '0':
                value = value[:last_char_index]
            else:
                break

    num = float(value) if value else 0.0

    if len(value) >= 2:
        last_two_chars_index_start = len(value) - 2
        last_two_chars = value[last_two_chars_index_start] + value[last_two_chars_index_start + 1]
    else:
        last_two_chars = ''

    if last_two_chars == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    else:
        if len(value) > 0:
            res = int(round(num))
        else:
            res = 0

    return res