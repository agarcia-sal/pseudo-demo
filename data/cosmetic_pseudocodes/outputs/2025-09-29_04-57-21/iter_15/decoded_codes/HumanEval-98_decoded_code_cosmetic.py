def count_upper(string_input: str) -> int:
    tally = 0
    position = 0
    while position < len(string_input):
        if string_input[position] in "AEIOU":
            tally += 1
        position += 2
    return tally