from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    temp_list: List[Union[int, float]] = []
    for idx in range(len(list_of_elements)):
        temp_list.append(list_of_elements[idx])
    n: int = len(temp_list)

    # Bubble sort
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if temp_list[j] > temp_list[j + 1]:
                holder = temp_list[j]
                temp_list[j] = temp_list[j + 1]
                temp_list[j + 1] = holder

    if (n & 1) != 0:
        return float(temp_list[(n - 1) // 2])

    mid_idx = (n // 2) - 1
    sum_val = temp_list[mid_idx] + temp_list[mid_idx + 1]
    result = 0.5 * sum_val
    return result