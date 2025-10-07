from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    parts = string_description.split(" ")
    idx = 0
    while idx < len(parts):
        curr_part = parts[idx]
        if not curr_part.isdigit():
            idx += 1
            continue
        num_val = int(curr_part)
        collected_numbers.append(num_val)
        idx += 1

    sum_numbers = 0
    for val in collected_numbers:
        sum_numbers += val

    return total_number_of_fruits - sum_numbers