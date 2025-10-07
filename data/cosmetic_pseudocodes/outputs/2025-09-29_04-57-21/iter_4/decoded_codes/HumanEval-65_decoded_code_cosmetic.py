def circular_shift(integer_x: int, integer_shift: int) -> str:
    text_form = str(integer_x)
    if integer_shift > len(text_form):
        return text_form[::-1]
    pivot = len(text_form) - integer_shift
    tail_part = text_form[pivot:]
    head_part = text_form[:pivot]
    return tail_part + head_part