from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_values: List[int] = []
    components: List[str] = string_description.split(" ")
    idx: int = 0
    while idx < len(components):
        token: str = components[idx]
        if token.isdigit():
            numeric_form: int = int(token)
            collected_values.append(numeric_form)
        idx += 1
    accumulated_sum: int = 0
    pos: int = 0
    while pos < len(collected_values):
        accumulated_sum += collected_values[pos]
        pos += 1
    return total_number_of_fruits - accumulated_sum