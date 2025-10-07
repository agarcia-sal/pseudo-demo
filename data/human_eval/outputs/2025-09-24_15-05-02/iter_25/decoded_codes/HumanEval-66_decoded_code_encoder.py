from typing import Union


def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    total_sum: int = 0
    for character in string_input:
        if character.isupper():
            total_sum += ord(character)
    return total_sum