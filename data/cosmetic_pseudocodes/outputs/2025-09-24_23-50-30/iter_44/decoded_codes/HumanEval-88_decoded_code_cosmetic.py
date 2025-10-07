from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not (len(input_list) != 0):
        return []
    first_and_last_total: int = input_list[0] + input_list[-1]
    is_descending: bool = (first_and_last_total % 2 == 0)
    return sorted(input_list, reverse=is_descending)