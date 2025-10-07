from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    for token in string_description.split(" "):
        if token.isdigit():
            numeric_value = int(token)
            collected_numbers.append(numeric_value)
    sum_of_collected = sum(collected_numbers)
    return total_number_of_fruits - sum_of_collected