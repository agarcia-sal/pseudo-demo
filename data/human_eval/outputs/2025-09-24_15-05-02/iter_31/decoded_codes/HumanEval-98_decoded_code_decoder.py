def count_upper(string_input: str) -> int:
    return sum(1 for i in range(0, len(string_input), 2) if string_input[i] in "AEIOU")