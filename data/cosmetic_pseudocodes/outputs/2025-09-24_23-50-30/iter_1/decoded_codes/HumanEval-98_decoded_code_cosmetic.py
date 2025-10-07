def count_upper(string_input: str) -> int:
    count = 0
    i = 0
    while i < len(string_input):
        if string_input[i] in "AEIOU":
            count += 1
        i += 2
    return count