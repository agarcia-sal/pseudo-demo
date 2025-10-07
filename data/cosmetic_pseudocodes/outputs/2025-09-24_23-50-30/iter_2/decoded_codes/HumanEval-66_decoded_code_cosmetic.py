def digitSum(string_input: str) -> int:
    total: int = 0
    index: int = len(string_input) - 1
    while index >= 0:
        char: str = string_input[index]
        if 'A' <= char <= 'Z':
            total += ord(char)
        index -= 1
    return total