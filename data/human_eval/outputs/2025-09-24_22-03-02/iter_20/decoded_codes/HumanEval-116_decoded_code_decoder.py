from typing import List, Tuple

def sort_array(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    result: List[Tuple[int, int]] = []
    for current_element in sorted_arr:
        binary_string = bin(current_element)[2:]
        count_ones = binary_string.count('1')
        result.append((count_ones, current_element))
    length_of_result = len(result)
    for i in range(length_of_result - 1):
        for j in range(length_of_result - 1 - i):
            if (result[j][0] > result[j + 1][0]) or (result[j][0] == result[j + 1][0] and result[j][1] > result[j + 1][1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    final_arr = [x[1] for x in result]
    return final_arr