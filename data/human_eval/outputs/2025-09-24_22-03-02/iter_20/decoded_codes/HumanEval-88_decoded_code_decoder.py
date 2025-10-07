from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    copy_array = list(array)
    sum_first_last = copy_array[0] + copy_array[-1]
    descending_flag = (sum_first_last % 2 == 0)
    n = len(copy_array)
    if descending_flag:
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if copy_array[j] < copy_array[j + 1]:
                    copy_array[j], copy_array[j + 1] = copy_array[j + 1], copy_array[j]
    else:
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if copy_array[j] > copy_array[j + 1]:
                    copy_array[j], copy_array[j + 1] = copy_array[j + 1], copy_array[j]
    return copy_array