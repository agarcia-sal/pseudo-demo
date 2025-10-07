from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    extracted_values: List[int] = []
    components: List[str] = string_description.split(" ")
    index: int = 0
    while index < len(components):
        token: str = components[index]
        if token.isdigit():
            extracted_values.append(int(token))
        index += 1
    accumulated_sum: int = sum(extracted_values)
    return total_number_of_fruits - accumulated_sum