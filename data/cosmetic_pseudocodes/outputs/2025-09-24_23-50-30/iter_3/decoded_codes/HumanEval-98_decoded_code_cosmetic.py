def count_upper(string_input: str) -> int:
    total: int = 0
    pos: int = 0
    while pos < len(string_input):
        if string_input[pos] in "AEIOU":
            total += 1
        pos += 2
    return total