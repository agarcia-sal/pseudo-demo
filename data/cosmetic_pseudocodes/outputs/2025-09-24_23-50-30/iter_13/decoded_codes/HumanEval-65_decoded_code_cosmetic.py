def circular_shift(integer_x: int, integer_shift: int) -> str:
    text_form = str(integer_x)
    if len(text_form) < integer_shift:
        return text_form[::-1]
    pivot = len(text_form) - integer_shift
    part_one = text_form[pivot:]
    part_two = text_form[:pivot]
    return part_one + part_two