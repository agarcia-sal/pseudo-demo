from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    parsed_numbers: List[int] = []
    tokens: List[str] = string_description.split(" ")
    position: int = 0
    while position < len(tokens):
        current_token = tokens[position]
        if '0' <= current_token <= '9':
            parsed_numbers.append(int(current_token))
        position += 1
    aggregated_sum: int = 0
    idx: int = 0
    while idx < len(parsed_numbers):
        aggregated_sum += parsed_numbers[idx]
        idx += 1
    return total_number_of_fruits - aggregated_sum