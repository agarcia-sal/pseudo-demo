from typing import Optional

def digitSum(input_string: Optional[str]) -> int:
    if not input_string:
        return 0
    total_sum: int = 0
    for character in input_string:
        if 'A' <= character <= 'Z':
            total_sum += ord(character)
    return total_sum