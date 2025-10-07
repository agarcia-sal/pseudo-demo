from typing import List

def COUNT_ONES(x: int) -> int:
    binary_string: List[int] = []
    n = abs(x)
    if n == 0:
        return 0
    while n > 0:
        remainder = n % 2
        binary_string.append(remainder)
        n = n // 2
    count = 0
    for i in range(len(binary_string)):
        if binary_string[i] == 1:
            count += 1
    return count

def sort_array(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    result = []
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            count_ones_min = COUNT_ONES(sorted_arr[min_index])
            count_ones_j = COUNT_ONES(sorted_arr[j])
            if count_ones_j < count_ones_min:
                min_index = j
            elif count_ones_j == count_ones_min:
                if sorted_arr[j] < sorted_arr[min_index]:
                    min_index = j
        if min_index != i:
            temp = sorted_arr[i]
            sorted_arr[i] = sorted_arr[min_index]
            sorted_arr[min_index] = temp
    result = sorted_arr
    return result