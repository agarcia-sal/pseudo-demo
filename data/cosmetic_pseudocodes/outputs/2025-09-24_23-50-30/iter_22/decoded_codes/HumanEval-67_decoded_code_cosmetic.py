from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numeric_values: List[int] = []
    tokens: List[str] = string_description.split(" ")
    idx: int = 0

    while idx < len(tokens):
        current_token: str = tokens[idx]
        if current_token.isdigit():
            numeric_values.append(int(current_token))
        idx += 1

    total_extracted: int = sum(numeric_values)
    return total_number_of_fruits - total_extracted