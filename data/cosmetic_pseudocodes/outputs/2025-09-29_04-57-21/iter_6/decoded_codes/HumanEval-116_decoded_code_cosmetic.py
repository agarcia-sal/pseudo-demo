from bisect import insort
from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones_in_binary(number: int) -> int:
        bits = ""
        n = number
        while n > 0:
            bits = chr(n % 2 + 48) + bits  # prepend '0' or '1'
            n //= 2
        ones_counter = sum(1 for bit in bits if bit == '1')
        return ones_counter

    temp_sorted_list: List[int] = []
    for num in array_of_integers:
        insort(temp_sorted_list, num)

    result_list: List[int] = []
    while temp_sorted_list:
        min_index = 0
        for j in range(1, len(temp_sorted_list)):
            count_j = count_ones_in_binary(temp_sorted_list[j])
            count_min = count_ones_in_binary(temp_sorted_list[min_index])
            if count_j < count_min or (count_j == count_min and temp_sorted_list[j] < temp_sorted_list[min_index]):
                min_index = j
        result_list.append(temp_sorted_list.pop(min_index))

    return result_list