def count_upper(string_input: str) -> int:
    tally: int = 0
    position: int = 0
    while position < len(string_input):
        if string_input[position] in "AEIOU":
            tally += 1
        position += 2
    return tally