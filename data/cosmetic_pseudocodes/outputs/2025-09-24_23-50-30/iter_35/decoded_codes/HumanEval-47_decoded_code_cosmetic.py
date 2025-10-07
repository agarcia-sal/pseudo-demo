from typing import List, Union

def insert_sorted(arr: List[Union[int, float]], x: Union[int, float]) -> None:
    if not arr:
        arr.append(x)
    else:
        index = 0
        while index < len(arr) and arr[index] < x:
            index += 1
        arr.insert(index, x)

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list: List[Union[int, float]] = []
    for element in list_of_elements:
        insert_sorted(sorted_list, element)

    total_count = len(sorted_list)
    midpoint = total_count // 2  # integer division for indexing

    if total_count % 2 == 1:
        return float(sorted_list[midpoint])
    else:
        left_val = sorted_list[midpoint - 1]
        right_val = sorted_list[midpoint]
        return (left_val + right_val) / 2.0