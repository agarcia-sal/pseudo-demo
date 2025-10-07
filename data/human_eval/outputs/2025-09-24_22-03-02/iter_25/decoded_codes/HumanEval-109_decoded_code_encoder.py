from typing import List

def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True

    sorted_array = sorted(arr)
    min_value = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] < min_value:
            min_value = arr[i]

    min_index = 0
    for i in range(n):
        if arr[i] == min_value:
            min_index = i
            break

    my_arr = arr[min_index:] + arr[:min_index]

    for i in range(n):
        if my_arr[i] != sorted_array[i]:
            return False

    return True