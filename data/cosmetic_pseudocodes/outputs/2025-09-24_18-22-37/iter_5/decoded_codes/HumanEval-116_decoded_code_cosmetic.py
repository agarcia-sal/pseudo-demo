from typing import List


def COUNT_ONES_IN_BINARY(num: int) -> int:
    binary_representation: str = bin(num)[2:]  # convert to binary string without '0b' prefix
    count_ones: int = 0
    k: int = 0
    while k < len(binary_representation):
        if binary_representation[k] == '1':
            count_ones += 1
        k += 1
    return count_ones


def sort_array(arr: List[int]) -> List[int]:
    idx: int = 0
    count_len: int = len(arr)
    temp_sorted_arr: List[int] = []
    while idx < count_len:
        temp_sorted_arr.append(arr[idx])
        idx += 1

    for i in range(len(temp_sorted_arr) - 1):
        for j in range(i + 1, len(temp_sorted_arr)):
            if temp_sorted_arr[i] > temp_sorted_arr[j]:
                temp = temp_sorted_arr[i]
                temp_sorted_arr[i] = temp_sorted_arr[j]
                temp_sorted_arr[j] = temp

    result: List[int] = []
    for i in range(len(temp_sorted_arr)):
        flag: bool = False
        for j in range(len(result)):
            ones_i = COUNT_ONES_IN_BINARY(temp_sorted_arr[i])
            ones_j = COUNT_ONES_IN_BINARY(result[j])
            if ones_i < ones_j:
                result.insert(j, temp_sorted_arr[i])
                flag = True
                break
            elif ones_i == ones_j:
                if temp_sorted_arr[i] < result[j]:
                    result.insert(j, temp_sorted_arr[i])
                    flag = True
                    break
        if not flag:
            result.append(temp_sorted_arr[i])

    return result