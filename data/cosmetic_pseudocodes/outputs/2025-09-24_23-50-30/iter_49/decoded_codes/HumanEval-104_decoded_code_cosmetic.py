from typing import List


def unique_digits(sequence_of_pos_ints: List[int]) -> List[int]:
    def all_digits_odd(number: int) -> bool:
        def check_digits(num: int, flag: bool) -> bool:
            if num == 0:
                return flag
            remainder = num % 10
            return check_digits(num // 10, flag and (remainder % 2 != 0))
        return check_digits(number, True)

    collected_odd_digit_items: List[int] = []

    def iterate_items(index: int) -> None:
        if index >= len(sequence_of_pos_ints):
            return
        current_item = sequence_of_pos_ints[index]
        if all_digits_odd(current_item):
            collected_odd_digit_items.append(current_item)
        iterate_items(index + 1)

    iterate_items(0)

    def merge_sort(arr: List[int]) -> List[int]:
        n = len(arr)
        if n <= 1:
            return arr
        midpoint = n // 2
        left_part = merge_sort(arr[:midpoint])
        right_part = merge_sort(arr[midpoint:])
        return merge(left_part, right_part)

    def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
        acc_be_sorted: List[int] = []
        i = 0
        j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                acc_be_sorted.append(left_arr[i])
                i += 1
            else:
                acc_be_sorted.append(right_arr[j])
                j += 1
        acc_be_sorted.extend(left_arr[i:])
        acc_be_sorted.extend(right_arr[j:])
        return acc_be_sorted

    return merge_sort(collected_odd_digit_items)