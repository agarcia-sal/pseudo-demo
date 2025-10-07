from typing import List, Union

def median(list_in: List[Union[int, float]]) -> Union[int, float, None]:
    if not list_in:
        return None  # Handle empty input gracefully
    sorted_arr: List[Union[int, float]] = []
    for i in range(len(list_in)):
        inserted = False
        for j in range(len(sorted_arr)):
            if list_in[i] < sorted_arr[j]:
                sorted_arr.insert(j, list_in[i])
                inserted = True
                break
        if not inserted:
            sorted_arr.append(list_in[i])

    length_val = len(sorted_arr)
    midpoint = length_val // 2

    if length_val % 2 != 0:
        return sorted_arr[midpoint]
    val1 = sorted_arr[midpoint]
    val0 = sorted_arr[midpoint - 1]
    return (val0 + val1) * 0.5