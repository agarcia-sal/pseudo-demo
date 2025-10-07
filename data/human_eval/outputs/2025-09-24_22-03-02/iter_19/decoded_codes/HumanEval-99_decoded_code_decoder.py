from typing import Union

def closest_integer(value: str) -> int:
    dot_count = 0
    i = 0
    length_value = len(value)
    while i < length_value:
        if value[i] == '.':
            dot_count += 1
        i += 1

    if dot_count == 1:
        j = len(value) - 1
        while j >= 0:
            if value[j] == '0':
                new_value = ''
                k = 0
                while k < j:
                    new_value += value[k]
                    k += 1
                value = new_value
                j -= 1
            else:
                break

    def to_float(v: str) -> float:
        result = 0.0
        negative = False
        start_idx = 0
        if v and v[0] == '-':
            negative = True
            start_idx = 1
        integer_part = 0
        fraction_part = 0.0
        fraction_divisor = 1.0
        decimal_found = False
        idx = start_idx
        while idx < len(v):
            c = v[idx]
            if c == '.':
                decimal_found = True
            else:
                digit = ord(c) - ord('0')
                if not decimal_found:
                    integer_part = integer_part * 10 + digit
                else:
                    fraction_divisor *= 10
                    fraction_part += digit / fraction_divisor
            idx += 1
        result = integer_part + fraction_part
        if negative:
            result = -result
        return result

    num = to_float(value)

    def string_ends_with(string: str, ending: str) -> bool:
        length_string = len(string)
        length_ending = len(ending)
        if length_ending > length_string:
            return False
        start_index = length_string - length_ending
        i = 0
        while i < length_ending:
            if string[start_index + i] != ending[i]:
                return False
            i += 1
        return True

    if string_ends_with(value, '.5'):
        def floor(x: float) -> int:
            if x >= 0:
                return int(x)
            else:
                int_part = int(x)
                if int_part != x:
                    int_part -= 1
                return int_part

        def ceil(x: float) -> int:
            from math import floor as math_floor
            if x == floor(x):
                return int(x)
            elif x > 0:
                return floor(x) + 1
            else:
                return floor(x)

        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        def floor(x: float) -> int:
            if x >= 0:
                return int(x)
            else:
                int_part = int(x)
                if int_part != x:
                    int_part -= 1
                return int_part

        def ceil(x: float) -> int:
            if x == floor(x):
                return int(x)
            elif x > 0:
                return floor(x) + 1
            else:
                return floor(x)

        def round_number(x: float) -> int:
            if x >= 0:
                floor_x = floor(x)
                diff = x - floor_x
                if diff >= 0.5:
                    return floor_x + 1
                else:
                    return floor_x
            else:
                ceil_x = ceil(x)
                diff = ceil_x - x
                if diff >= 0.5:
                    return ceil_x - 1
                else:
                    return ceil_x

        res = round_number(num)
    else:
        res = 0

    return res