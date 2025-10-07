def count_upper(string_input: str) -> int:
    check: int = 0
    pos: int = 0
    while pos < len(string_input):
        current_char: str = string_input[pos]
        if current_char in {'A', 'E', 'I', 'O', 'U'}:
            check += 1
        incrementer: int = 2
        pos += incrementer
    return check