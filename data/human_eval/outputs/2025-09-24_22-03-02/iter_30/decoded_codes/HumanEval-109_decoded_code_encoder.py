from typing import List

def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True

    sorted_array = sorted(arr)
    min_value = arr[0]
    min_index = 0
    i = 1
    while i < len(arr):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
        i += 1

    temp_list1 = []
    j = min_index
    while j < len(arr):
        temp_list1.append(arr[j])
        j += 1

    temp_list2 = []
    k = 0
    while k < min_index:
        temp_list2.append(arr[k])
        k += 1

    my_arr = temp_list1 + temp_list2

    l = 0
    while l < len(arr):
        if my_arr[l] != sorted_array[l]:
            return False
        l += 1

    return True