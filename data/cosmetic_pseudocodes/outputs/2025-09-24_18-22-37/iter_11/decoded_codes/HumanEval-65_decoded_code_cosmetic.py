def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_string: str = str(integer_x)
    str_length: int = len(temp_string)

    if integer_shift > str_length:
        reversed_string = ''.join(temp_string[i] for i in range(str_length - 1, -1, -1))
        return reversed_string
    else:
        pivot = str_length - integer_shift
        first_part = ''.join(temp_string[i] for i in range(pivot, str_length))
        second_part = ''.join(temp_string[i] for i in range(pivot))
        result_string = first_part + second_part
        return result_string