from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    words = string_description.split(" ")
    index = 0
    while index < len(words):
        current_token = words[index]
        if current_token.isdigit():
            numeric_value = int(current_token)
            collected_numbers.append(numeric_value)
        index += 1
    sum_numbers = 0
    pos = 0
    while pos < len(collected_numbers):
        sum_numbers += collected_numbers[pos]
        pos += 1
    return total_number_of_fruits - sum_numbers