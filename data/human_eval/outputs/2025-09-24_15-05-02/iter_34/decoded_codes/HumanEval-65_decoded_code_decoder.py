def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_representation = str(integer_x)
    length = len(string_representation)
    if integer_shift > length:
        return string_representation[::-1]
    else:
        split_index = length - integer_shift
        return string_representation[split_index:] + string_representation[:split_index]