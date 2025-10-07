def count_upper(string_input: str) -> int:
    count = 0
    for index in range(0, len(string_input), 2):
        if string_input[index] in "AEIOU":
            count += 1
    return count