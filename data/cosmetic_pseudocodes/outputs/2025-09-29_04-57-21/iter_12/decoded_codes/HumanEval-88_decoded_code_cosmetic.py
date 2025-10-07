from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not input_list:
        return []

    total_of_edges: int = input_list[0] + input_list[-1]
    descending_flag: bool = (total_of_edges % 2 == 0)

    result_sorted: List[int] = sorted(input_list)
    if descending_flag:
        result_sorted.reverse()

    return result_sorted