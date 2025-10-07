from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    elements: List[str] = string_description.split(" ")
    idx: int = 0

    while idx < len(elements):
        current_token: str = elements[idx]
        if current_token.isdigit():
            converted_number: int = int(current_token)
            collected_numbers.append(converted_number)
        idx += 1

    accumulated_sum: int = 0
    number_idx: int = 0
    while number_idx < len(collected_numbers):
        current_value: int = collected_numbers[number_idx]
        accumulated_sum += current_value
        number_idx += 1

    result: int = total_number_of_fruits - accumulated_sum
    return result