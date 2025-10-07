def count_upper(string_input: str) -> int:
    tally = 0
    position = 0

    while position < len(string_input):
        current_char = string_input[position]
        if current_char in {'A', 'E', 'I', 'O', 'U'}:
            tally += 1
        position += 2

    return tally