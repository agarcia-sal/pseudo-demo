from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    tokens: List[str] = string_description.split(" ")
    idx: int = 0

    while idx < len(tokens):
        current_token: str = tokens[idx]
        if current_token.isdigit():
            collected_values.append(int(current_token))
        idx += 1

    accumulated_sum: int = sum(collected_values)
    return total_number_of_fruits - accumulated_sum