def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_x = str(integer_x)

    if integer_shift > len(str_x):
        reversed_str = ''.join(str_x[i] for i in range(len(str_x) - 1, -1, -1))
        return reversed_str

    length = len(str_x)
    start_index = length - integer_shift
    result = str_x[start_index:] + str_x[:start_index]

    return result