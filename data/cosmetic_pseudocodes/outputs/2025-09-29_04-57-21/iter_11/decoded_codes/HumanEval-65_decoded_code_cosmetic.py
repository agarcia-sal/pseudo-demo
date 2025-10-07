def circular_shift(integer_x: int, integer_shift: int) -> str:
    text_form: str = str(integer_x)
    if len(text_form) < integer_shift:
        return text_form[::-1]
    pivot: int = len(text_form) - integer_shift
    tail_segment: str = text_form[pivot:]
    head_segment: str = text_form[:pivot]
    return tail_segment + head_segment