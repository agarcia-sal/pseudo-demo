from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    intermediate_sorted_list = sorted(input_list)
    # Sort by number of '1's in binary representation excluding '0b' prefix
    result_list = sorted(
        intermediate_sorted_list,
        key=lambda curr_item: bin(curr_item)[2:].count('1')
    )
    return result_list