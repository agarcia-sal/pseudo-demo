from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_odd_only: List[int] = []
    idx: int = 0
    while idx < len(list_of_positive_integers):
        current_value = list_of_positive_integers[idx]
        digits_are_all_odd = True
        digit_string = str(current_value)
        pos = 0
        while pos < len(digit_string):
            digit_char = digit_string[pos]
            digit_num = int(digit_char)
            if digit_num % 2 == 0:  # even digit found
                digits_are_all_odd = False
                break
            pos += 1
        if digits_are_all_odd:
            collected_odd_only.append(current_value)
        idx += 1

    result_sorted: List[int] = []
    unsorted_list = collected_odd_only[:]
    while len(unsorted_list) > 0:
        smallest_value = unsorted_list[0]
        smallest_index = 0
        scan_index = 1
        while scan_index < len(unsorted_list):
            if unsorted_list[scan_index] < smallest_value:
                smallest_value = unsorted_list[scan_index]
                smallest_index = scan_index
            scan_index += 1
        result_sorted.append(smallest_value)
        unsorted_list.pop(smallest_index)
    return result_sorted