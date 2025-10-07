from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    tokens = string_description.split()
    current_index = 0

    while current_index < len(tokens):
        item = tokens[current_index]
        if item.isdigit():
            collected_values.append(int(item))
        current_index += 1

    return total_number_of_fruits - sum(collected_values)