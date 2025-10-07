def circular_shift(integer_x: int, integer_shift: int) -> str:
    text_form = str(integer_x)
    length_text = len(text_form)

    if not (integer_shift <= length_text):
        return text_form[::-1]

    pivot = length_text - integer_shift
    tail_portion = text_form[pivot:length_text]
    head_portion = text_form[0:pivot]

    return tail_portion + head_portion