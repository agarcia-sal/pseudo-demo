from typing import List


def sort_array(fresh_list: List[int]) -> List[int]:
    def helper_sort(index: int, fresh_accumulated: List[int]) -> List[int]:
        if index == len(fresh_list):
            return fresh_list  # Actual sorted list is fresh_list after in-place swaps
        min_pos = index
        for iterator in range(index + 1, len(fresh_list)):
            if fresh_list[iterator] < fresh_list[min_pos]:
                min_pos = iterator
        fresh_list[index], fresh_list[min_pos] = fresh_list[min_pos], fresh_list[index]
        return helper_sort(index + 1, fresh_accumulated)

    fresh_sorted_decimal = helper_sort(0, [])

    def count_one_bits(number: int) -> int:
        fresh_count = 0
        fresh_num = number
        while fresh_num > 0:
            fresh_count += fresh_num % 2
            fresh_num //= 2
        return fresh_count

    fresh_length = len(fresh_sorted_decimal)
    fresh_index = 0
    while fresh_index < fresh_length - 1:
        if count_one_bits(fresh_sorted_decimal[fresh_index]) > count_one_bits(fresh_sorted_decimal[fresh_index + 1]):
            fresh_sorted_decimal[fresh_index], fresh_sorted_decimal[fresh_index + 1] = (
                fresh_sorted_decimal[fresh_index + 1],
                fresh_sorted_decimal[fresh_index],
            )
            fresh_index = 0
        else:
            fresh_index += 1

    return fresh_sorted_decimal