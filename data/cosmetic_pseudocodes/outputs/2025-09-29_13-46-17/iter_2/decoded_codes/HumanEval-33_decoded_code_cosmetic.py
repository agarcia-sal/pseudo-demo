from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    def helper(index: int, arr: List[int], sorted_vals: List[int]) -> List[int]:
        if index >= len(arr):
            return arr
        arr[index] = sorted_vals[index // 3]
        return helper(index + 3, arr, sorted_vals)

    copy_list = list(list_input)  # make a shallow copy
    filtered_vals = [copy_list[idx] for idx in range(len(copy_list)) if idx % 3 == 0]
    sorted_filtered_vals = sorted(filtered_vals)
    return helper(0, copy_list, sorted_filtered_vals)