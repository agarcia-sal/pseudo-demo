from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    elements_iterator = string_description.split(" ")

    current_position = 0
    while current_position < len(elements_iterator):
        token = elements_iterator[current_position]
        if token.isdigit():
            collected_values.append(int(token))
        current_position += 1

    accumulated_sum = sum(collected_values)
    return total_number_of_fruits - accumulated_sum