from typing import List


def sort_array(arr: List[int]) -> List[int]:
    total: int = 0
    ordering_flag: bool = False
    if len(arr) != 0:
        first_element: int = arr[0]
        last_index: int = len(arr) - 1
        last_element: int = arr[last_index]
        total = first_element + last_element
        if total % 2 == 0:
            ordering_flag = True
        else:
            ordering_flag = False
        copy_arr: List[int] = [element for element in arr]
        i: int = 1
        while i < len(copy_arr):
            j: int = i
            # insertion sort variant based on ordering_flag
            while j > 0 and (
                (ordering_flag and copy_arr[j - 1] < copy_arr[j]) or
                (not ordering_flag and copy_arr[j - 1] > copy_arr[j])
            ):
                copy_arr[j], copy_arr[j - 1] = copy_arr[j - 1], copy_arr[j]
                j -= 1
            i += 1
        return copy_arr
    else:
        return []