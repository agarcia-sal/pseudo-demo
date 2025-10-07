from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    acc_values: List[int] = []
    array_elements = string_description.split(" ")
    idx = 0
    while idx < len(array_elements):
        cur_val = array_elements[idx]
        if cur_val.isdigit():
            acc_values.append(int(cur_val))
        idx += 1
    total_used = 0
    ptr = 0
    while ptr < len(acc_values):
        total_used += acc_values[ptr]
        ptr += 1
    return total_number_of_fruits - total_used