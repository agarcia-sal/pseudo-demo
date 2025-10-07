def count_upper(string_input: str) -> int:
    total: int = 0
    cursor: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while cursor < len(string_input):
        current_char = string_input[cursor]
        if current_char in vowels:
            total += 1
        cursor += 2
    return total