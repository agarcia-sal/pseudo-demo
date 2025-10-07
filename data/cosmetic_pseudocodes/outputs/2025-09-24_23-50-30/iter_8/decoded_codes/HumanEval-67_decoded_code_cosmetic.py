from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0
    array_of_tokens: List[str] = string_description.split(" ")
    index: int = 0
    while index < len(array_of_tokens):
        current: str = array_of_tokens[index]
        if current.isdigit():
            accumulator += int(current)
        index += 1
    return total_number_of_fruits - accumulator