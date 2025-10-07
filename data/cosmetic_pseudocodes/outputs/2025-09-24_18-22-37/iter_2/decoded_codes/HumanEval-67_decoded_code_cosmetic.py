from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    extracted_values: List[int] = [int(token) for token in string_description.split() if token.isdigit()]
    sum_values: int = sum(extracted_values)
    return total_number_of_fruits - sum_values