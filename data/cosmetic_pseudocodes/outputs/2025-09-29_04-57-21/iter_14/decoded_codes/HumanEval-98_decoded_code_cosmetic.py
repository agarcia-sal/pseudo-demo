def count_upper(string_input: str) -> int:
    tally: int = 0
    position: int = 0
    while position < len(string_input):
        current_char: str = string_input[position]
        if current_char in "AEIOU":
            tally += 1
        position += 2
    return tally