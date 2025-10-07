def digitSum(string_input: str) -> int:
    accumulator: int = 0
    index: int = 0

    while index < len(string_input):
        current_char: str = string_input[index]
        if 'A' <= current_char <= 'Z':
            accumulator += ord(current_char)
        index += 1

    return accumulator