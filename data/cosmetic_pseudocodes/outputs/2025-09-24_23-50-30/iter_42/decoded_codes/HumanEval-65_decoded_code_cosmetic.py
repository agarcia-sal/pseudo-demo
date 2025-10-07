def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_values = str(integer_x)
    if integer_shift > len(string_values):
        return string_values[::-1]
    length_val = len(string_values)
    index_val = length_val - integer_shift
    front_part = string_values[index_val:length_val]
    back_part = string_values[0:index_val]
    return front_part + back_part