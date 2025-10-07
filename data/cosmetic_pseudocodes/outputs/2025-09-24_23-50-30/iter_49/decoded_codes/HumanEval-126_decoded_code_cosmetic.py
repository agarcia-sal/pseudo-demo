from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    def accumulate_counts(index: int, tally: Dict[int, int]) -> Dict[int, int]:
        if index >= len(list_of_numbers):
            return tally
        current_item = list_of_numbers[index]
        tally[current_item] = tally.get(current_item, 0) + 1
        return accumulate_counts(index + 1, tally)

    def has_value_exceeding_two(keys: List[int], map_: Dict[int, int]) -> bool:
        for idx in range(len(keys)):
            if map_[keys[idx]] > 2:
                return True
        return False

    def non_decreasing_check(pos: int) -> bool:
        if pos >= len(list_of_numbers):
            return True
        if list_of_numbers[pos - 1] <= list_of_numbers[pos]:
            return non_decreasing_check(pos + 1)
        return False

    accumulated_counts = accumulate_counts(0, {})
    unique_keys = list(accumulated_counts.keys())

    if has_value_exceeding_two(unique_keys, accumulated_counts):
        return False
    return non_decreasing_check(1)