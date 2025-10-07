from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numeric_values: List[int] = []

    def process_elements(elements: List[str], idx: int) -> None:
        if idx == len(elements):
            return
        current_element = elements[idx]
        if current_element.isdigit():
            numeric_values.append(int(current_element))
        process_elements(elements, idx + 1)

    tokens = string_description.split(" ")
    process_elements(tokens, 0)
    accumulated_sum = 0
    for value in numeric_values:
        accumulated_sum += value
    return total_number_of_fruits - accumulated_sum