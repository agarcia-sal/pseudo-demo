from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0
    tokens: List[str] = string_description.split(" ")
    for current_token in tokens:
        if current_token.isdigit():
            accumulator += int(current_token)
    return total_number_of_fruits - accumulator