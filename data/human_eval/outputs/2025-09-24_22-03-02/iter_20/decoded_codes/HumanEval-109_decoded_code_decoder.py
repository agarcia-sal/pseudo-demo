from typing import List


def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True

    sorted_array = sorted(arr)
    my_arr = []

    min_value = min(arr)
    min_index = arr.index(min_value)

    for i in range(min_index, len(arr)):
        my_arr.append(arr[i])

    for i in range(min_index):
        my_arr.append(arr[i])

    for i in range(len(arr)):
        if my_arr[i] != sorted_array[i]:
            return False

    return True