from typing import AnyStr

def digitSum(input_str: AnyStr) -> int:
    total_value: int = 0
    iterator: int = 0
    length: int = len(input_str)
    while iterator < length:
        current_char: str = input_str[iterator]
        if 'A' <= current_char <= 'Z':
            total_value += ord(current_char)
        else:
            total_value += 0
        iterator += 1
    if length == 0:
        return 0
    return total_value