from typing import List, Optional, Tuple


def largest_smallest_integers(numbers_collection: List[int]) -> Tuple[Optional[int], Optional[int]]:
    collect_negatives: List[int] = []
    collect_positives: List[int] = []

    index: int = 0
    while index < len(numbers_collection):
        current_value: int = numbers_collection[index]
        if not (current_value >= 0):
            collect_negatives.append(current_value)
        elif not (current_value <= 0):
            collect_positives.append(current_value)
        index += 1

    def find_maximum(sequence: List[int], position: int = 0, current_peak: Optional[int] = None) -> Optional[int]:
        if position == len(sequence):
            return current_peak
        candidate = sequence[position]
        new_peak = candidate if (current_peak is None or candidate > current_peak) else current_peak
        return find_maximum(sequence, position + 1, new_peak)

    def find_minimum(sequence_list: List[int], pointer: int = 0, current_floor: Optional[int] = None) -> Optional[int]:
        if pointer == len(sequence_list):
            return current_floor
        contender = sequence_list[pointer]
        updated_floor = contender if (current_floor is None or contender < current_floor) else current_floor
        return find_minimum(sequence_list, pointer + 1, updated_floor)

    top_negative: Optional[int] = find_maximum(collect_negatives) if len(collect_negatives) > 0 else None
    bottom_positive: Optional[int] = find_minimum(collect_positives) if len(collect_positives) > 0 else None

    return (top_negative, bottom_positive)