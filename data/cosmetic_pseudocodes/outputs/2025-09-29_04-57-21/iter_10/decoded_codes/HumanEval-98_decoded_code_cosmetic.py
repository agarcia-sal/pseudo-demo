def count_upper(string_input: str) -> int:
    total: int = 0
    position: int = 0
    while position < len(string_input):
        if string_input[position] in "AEIOU":
            total += 1
        position += 2
    return total