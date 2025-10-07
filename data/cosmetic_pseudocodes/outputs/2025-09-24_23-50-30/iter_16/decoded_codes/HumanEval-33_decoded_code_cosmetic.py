from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    temp_list: List[int] = [x for x in list_input]

    divisible_indices: List[int] = []
    filtered_vals: List[int] = []
    current_index: int = 0

    while current_index < len(temp_list):
        if current_index % 3 == 0:
            divisible_indices.append(current_index)
            filtered_vals.append(temp_list[current_index])
        current_index += 1

    ordered_vals: List[int] = []
    min_val: int = min(filtered_vals) - 1
    while len(ordered_vals) < len(filtered_vals):
        # Find max x in filtered_vals where x > min_val
        next_val_candidates = [x for x in filtered_vals if x > min_val]
        next_val = max(next_val_candidates)
        ordered_vals.append(next_val)
        min_val = next_val

    place_index: int = 0
    while place_index < len(divisible_indices):
        temp_list[divisible_indices[place_index]] = ordered_vals[place_index]
        place_index += 1

    return temp_list