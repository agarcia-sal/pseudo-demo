def circular_shift(integer_x: int, integer_shift: int) -> str:
    text_form: str = str(integer_x)
    if integer_shift > len(text_form):
        return text_form[::-1]
    pivot: int = len(text_form) - integer_shift
    tail_slice: str = text_form[pivot:]
    head_slice: str = text_form[:pivot]
    return tail_slice + head_slice