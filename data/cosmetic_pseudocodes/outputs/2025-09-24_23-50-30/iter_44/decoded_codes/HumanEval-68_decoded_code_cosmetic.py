from typing import List, Optional, Tuple, Union


def pluck(list_of_items: List[int]) -> List[Union[int, int]]:
    def find_min_even_index(
        curr_list: List[int],
        curr_index: int,
        curr_min_value: Optional[int],
        curr_min_index: Optional[int],
    ) -> Tuple[Optional[int], Optional[int]]:
        if curr_index >= len(curr_list):
            return curr_min_value, curr_min_index
        candidate = curr_list[curr_index]
        if candidate % 2 == 0 and (curr_min_value is None or candidate < curr_min_value):
            return find_min_even_index(curr_list, curr_index + 1, candidate, curr_index)
        return find_min_even_index(curr_list, curr_index + 1, curr_min_value, curr_min_index)

    if len(list_of_items) == 0:
        return []

    min_even, min_even_pos = find_min_even_index(list_of_items, 0, None, None)

    if min_even is None:
        return []
    return [min_even, min_even_pos]