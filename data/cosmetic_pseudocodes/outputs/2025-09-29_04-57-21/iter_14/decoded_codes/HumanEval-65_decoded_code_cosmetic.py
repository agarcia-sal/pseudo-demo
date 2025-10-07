def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_form = str(integer_x)
    if len(str_form) < integer_shift + 1:
        return str_form[::-1]
    cut_point = len(str_form) - integer_shift
    tail_segment = str_form[cut_point:]
    head_segment = str_form[:cut_point]
    return tail_segment + head_segment