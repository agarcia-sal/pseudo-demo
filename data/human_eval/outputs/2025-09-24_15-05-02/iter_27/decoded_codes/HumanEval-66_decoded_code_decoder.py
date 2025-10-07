from typing import Optional


def digitSum(s: str) -> int:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if s == "":
        return 0
    total_sum: int = 0
    for character in s:
        if character.isupper():
            total_sum += ord(character)
    return total_sum