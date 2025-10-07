from typing import List, Dict

def by_length(obtained_array: List[int]) -> List[str]:
    alphanumeric_map: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    def recursive_accumulate(descending_arr: List[int], counting_index: int, accumulated_arr: List[str]) -> List[str]:
        if counting_index < 0:
            return accumulated_arr
        current_value = descending_arr[counting_index]
        if current_value in alphanumeric_map:
            updated_arr = accumulated_arr + [alphanumeric_map[current_value]]
        else:
            updated_arr = accumulated_arr
        return recursive_accumulate(descending_arr, counting_index - 1, updated_arr)

    descending_order_arr = sorted(obtained_array, reverse=True)
    return recursive_accumulate(descending_order_arr, len(descending_order_arr) - 1, [])