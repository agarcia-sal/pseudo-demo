from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    extracted_numbers: List[int] = []
    tokens = string_description.split(' ')
    idx = 0
    while idx < len(tokens):
        current_token = tokens[idx]
        if current_token.isdigit():
            numeric_value = int(current_token)
            extracted_numbers.append(numeric_value)
        idx += 1
    sum_numbers = 0
    iterator = 0
    while iterator < len(extracted_numbers):
        sum_numbers += extracted_numbers[iterator]
        iterator += 1
    return total_number_of_fruits - sum_numbers