from typing import List

def strange_sort_list(unseen_array: List[int]) -> List[int]:
    def loop(accumulated_result: List[int], flag: bool, remaining_values: List[int]) -> List[int]:
        if not remaining_values:
            return accumulated_result
        chosen_element = min(remaining_values) if flag else max(remaining_values)
        new_result = accumulated_result + [chosen_element]
        filtered_remaining = [item for item in remaining_values if item != chosen_element]
        return loop(new_result, not flag, filtered_remaining)
    return loop([], True, unseen_array)