def count_upper(string_input: str) -> int:
    tally: int = 0
    pos: int = 0
    while pos < len(string_input):
        if string_input[pos] in "AEIOU":
            tally += 1
        pos += 2
    return tally