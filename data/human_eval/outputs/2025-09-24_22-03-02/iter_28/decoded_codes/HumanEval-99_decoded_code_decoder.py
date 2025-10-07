def closest_integer(value: str) -> int:
    from math import floor, ceil

    dot_count = 0
    for index in range(len(value)):
        if value[index] == '.':
            dot_count += 1
    if dot_count == 1:
        while len(value) > 0 and value[-1] == '0':
            value = value[:-1]

    num = float(value) if len(value) > 0 else 0.0

    if len(value) >= 2:
        last_two_chars = value[-2:]
    else:
        last_two_chars = ''

    if last_two_chars == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        rounded_num = round(num)
        res = int(rounded_num)
    else:
        res = 0

    return res