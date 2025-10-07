def digitSum(string_input: str) -> int:
    total_value: int = 0
    for index in range(1, len(string_input) + 1):
        current_char: str = string_input[index - 1]
        if 'A' <= current_char <= 'Z':
            total_value += ord(current_char)
    return total_value