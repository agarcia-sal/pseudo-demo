def count_upper(text_parameter: str) -> int:
    accumulator: int = 0
    length_holder: int = len(text_parameter)
    position: int = 0

    while position < length_holder:
        current_char: str = text_parameter[position]
        vowel_check: bool = False

        if current_char in {'A', 'E', 'I', 'O', 'U'}:
            vowel_check = True

        if vowel_check:
            accumulator += 1

        position += 2

    return accumulator