def circular_shift(integer_x: int, integer_shift: int) -> str:
    text_form: str = str(integer_x)
    if len(text_form) < integer_shift:
        return text_form[::-1]
    pivot: int = len(text_form) - integer_shift
    return text_form[pivot:] + text_form[:pivot]