from typing import List


def unique_digits(arr_of_pos_ints: List[int]) -> List[int]:
    def are_all_digits_odd(num: int, acc: bool) -> bool:
        if num == 0:
            return acc
        digit = num % 10
        is_odd_digit = (digit % 2) != 0
        return are_all_digits_odd(num // 10, acc and is_odd_digit)

    def gather_odd_digits_elements(input_list: List[int], index: int, result_stack: List[int]) -> List[int]:
        if index >= len(input_list):
            return result_stack
        current_value = input_list[index]
        if are_all_digits_odd(current_value, True):
            return gather_odd_digits_elements(input_list, index + 1, result_stack + [current_value])
        else:
            return gather_odd_digits_elements(input_list, index + 1, result_stack)

    filtered_list = gather_odd_digits_elements(arr_of_pos_ints, 0, [])

    sorted_filtered = filtered_list[:]
    n = len(sorted_filtered)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_filtered[j] > sorted_filtered[j + 1]:
                sorted_filtered[j], sorted_filtered[j + 1] = sorted_filtered[j + 1], sorted_filtered[j]

    return sorted_filtered