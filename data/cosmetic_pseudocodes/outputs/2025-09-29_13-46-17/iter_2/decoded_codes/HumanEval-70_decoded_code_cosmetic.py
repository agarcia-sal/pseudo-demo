from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def helper(input_list: List[int], pick_min: bool, accum: List[int]) -> List[int]:
        if not input_list:
            return accum
        chosen_value = min(input_list) if pick_min else max(input_list)
        # Remove first occurrence of chosen_value
        trimmed_list = input_list.copy()
        trimmed_list.remove(chosen_value)
        return helper(trimmed_list, not pick_min, accum + [chosen_value])

    return helper(list_of_integers, True, [])