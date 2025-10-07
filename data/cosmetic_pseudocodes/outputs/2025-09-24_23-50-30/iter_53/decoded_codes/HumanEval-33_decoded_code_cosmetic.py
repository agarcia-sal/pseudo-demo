from typing import List

def sort_third(array_data: List[int]) -> List[int]:
    def gather_indices(idx: int, accu: List[int]) -> List[int]:
        if idx >= len(array_data):
            return accu
        return gather_indices(idx + 3, accu + [array_data[idx]])

    def place_indices(idx: int, values: List[int], arr: List[int]) -> List[int]:
        if idx >= len(arr):
            return arr
        arr_updated = arr.copy()
        arr_updated[idx] = values[0]
        return place_indices(idx + 3, values[1:], arr_updated)

    temp_arr: List[int] = []
    for i in range(len(array_data)):
        temp_arr = temp_arr + [array_data[i]]

    extracted = gather_indices(0, [])
    sorted_extracted = sorted(extracted)

    result_arr = place_indices(0, sorted_extracted, temp_arr)

    return result_arr