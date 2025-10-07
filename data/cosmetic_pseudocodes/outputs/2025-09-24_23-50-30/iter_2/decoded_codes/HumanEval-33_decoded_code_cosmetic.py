from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    temp_list: List[int] = []
    for i in range(len(list_input) - 1, -1, -1):
        if i % 3 != 0:
            continue
        temp_list.insert(0, list_input[i])  # Prepend element at multiples of 3
    temp_list.sort()

    def helper(index: int, arr: List[int], values: List[int]) -> List[int]:
        if index >= len(arr):
            return arr
        if index % 3 == 0:
            arr[index] = values[0]
            return helper(index + 1, arr, values[1:])
        else:
            return helper(index + 1, arr, values)

    return helper(0, list_input.copy(), temp_list)