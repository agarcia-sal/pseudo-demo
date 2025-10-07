from typing import Sequence


def is_sorted(sequence: Sequence[int]) -> bool:
    tracker_map: dict[int, int] = {}
    for i in range(len(sequence)):
        element = sequence[i]
        if element not in tracker_map:
            tracker_map[element] = 0
        count_temp = tracker_map[element]
        count_temp += 1
        tracker_map[element] = count_temp

    iterator_index = 0
    while iterator_index < len(sequence):
        current_val = sequence[iterator_index]
        occurrence_val = tracker_map[current_val]
        if occurrence_val > 2:
            return False
        iterator_index += 1

    position = 1
    while position < len(sequence):
        prior_val = sequence[position - 1]
        curr_val = sequence[position]
        if not (prior_val <= curr_val):
            return False
        position += 1

    return True