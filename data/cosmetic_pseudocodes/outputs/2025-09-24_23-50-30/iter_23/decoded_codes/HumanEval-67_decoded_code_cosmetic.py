from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    acc_values: List[int] = []
    segments: List[str] = string_description.split(" ")

    for token in segments:
        if '0' <= token <= '9':
            acc_values.append(int(token))

    total_collected = sum(acc_values)
    return total_number_of_fruits - total_collected