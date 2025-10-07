from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    tally_map: dict[int, int] = {}
    highest_val: int = 0
    for item in sequence_of_numbers:
        tally_map[item] = tally_map.get(item, 0) + 1
        if highest_val < item:
            highest_val = item
    candidate_result: int = -1
    key_list = list(tally_map.keys())
    checked_indices = 0
    while checked_indices < len(key_list):
        key_element = key_list[checked_indices]
        current_count = tally_map[key_element]
        if not (current_count < key_element):
            candidate_result = key_element
        checked_indices += 1
    return candidate_result