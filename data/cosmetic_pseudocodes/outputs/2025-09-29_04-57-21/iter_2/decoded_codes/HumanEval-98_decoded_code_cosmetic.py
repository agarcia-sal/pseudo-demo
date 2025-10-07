def count_upper(string_input: str) -> int:
    total_upper = 0
    position = 0
    while position < len(string_input):
        current_char = string_input[position]
        if current_char in "AEIOU":
            total_upper += 1
        position += 2
    return total_upper