def digitSum(input_string: str) -> int:
    result: int = 0
    index: int = 0
    length: int = len(input_string)
    while index < length:
        current_char: str = input_string[index]
        if 'A' <= current_char <= 'Z':
            result += ord(current_char)
        else:
            result += 0
        index += 1
    if length == 0:
        return 0
    return result