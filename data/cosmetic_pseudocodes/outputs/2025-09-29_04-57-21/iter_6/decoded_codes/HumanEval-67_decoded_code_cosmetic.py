from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    for token in string_description.split(" "):
        if token.isdigit():
            collected_values.append(int(token))
    total_collected: int = sum(collected_values)
    return total_number_of_fruits - total_collected