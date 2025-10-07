from typing import Optional, Sequence

def next_smallest(collection_of_numbers: Sequence[int]) -> Optional[int]:
    filtered_list: list[int] = []
    tracker_map: dict[int, bool] = {}

    idx_counter: int = 0
    while idx_counter < len(collection_of_numbers):
        current_val = collection_of_numbers[idx_counter]
        if current_val not in tracker_map:
            tracker_map[current_val] = True
            filtered_list.append(current_val)
        idx_counter += 1

    filtered_list.sort()

    if len(filtered_list) < 2:
        return None

    return filtered_list[1]