from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    extracted_values: List[int] = []
    tokens: List[str] = string_description.split(" ")
    for token in tokens:
        if token.isdigit():
            extracted_values.append(int(token))
    accumulated_total: int = sum(extracted_values)
    return total_number_of_fruits - accumulated_total