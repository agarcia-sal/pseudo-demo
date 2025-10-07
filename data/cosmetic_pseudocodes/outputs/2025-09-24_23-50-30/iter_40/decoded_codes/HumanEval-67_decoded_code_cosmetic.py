from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0
    elements: List[str] = string_description.split(" ")
    for fragment in elements:
        if fragment.isdigit():
            accumulator += int(fragment)
    return total_number_of_fruits - accumulator