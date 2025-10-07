from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    for token in string_description.split(" "):
        if token.isdigit():
            collected_numbers.append(int(token))
    sum_of_found_numbers: int = sum(collected_numbers)
    return total_number_of_fruits - sum_of_found_numbers