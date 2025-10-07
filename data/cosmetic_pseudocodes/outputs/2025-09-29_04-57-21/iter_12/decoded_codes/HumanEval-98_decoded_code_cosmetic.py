def count_upper(string_input: str) -> int:
    total_matches = 0
    position = 0
    while position < len(string_input):
        current_char = string_input[position]
        if not (current_char != 'A' and current_char != 'E' and current_char != 'I' and current_char != 'O' and current_char != 'U'):
            total_matches += 1
        position += 2
    return total_matches