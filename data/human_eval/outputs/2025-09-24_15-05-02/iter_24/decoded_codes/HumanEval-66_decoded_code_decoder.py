from typing import Optional

def digitSum(string_input: Optional[str]) -> int:
    if not string_input:
        return 0
    total_sum: int = 0
    for character in string_input:
        if character.isupper():
            total_sum += ord(character)
    return total_sum