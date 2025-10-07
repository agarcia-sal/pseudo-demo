from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    index: int = 0
    tokens: List[str] = string_description.split()
    while index < len(tokens):
        current_token = tokens[index]
        if current_token.isdigit():
            numeric_value = int(current_token)
            collected_numbers.append(numeric_value)
        index += 1

    sum_of_numbers: int = 0
    position: int = 0
    while position < len(collected_numbers):
        sum_of_numbers += collected_numbers[position]
        position += 1

    remaining_fruits = total_number_of_fruits - sum_of_numbers
    return remaining_fruits