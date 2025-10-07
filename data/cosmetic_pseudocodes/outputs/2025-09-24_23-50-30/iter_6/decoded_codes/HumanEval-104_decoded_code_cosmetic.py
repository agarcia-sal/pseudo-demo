from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_collection: List[int] = []
    idx: int = 0
    while idx < len(list_of_positive_integers):
        current_value: int = list_of_positive_integers[idx]

        digits_list: List[int] = []
        temp_val: int = current_value
        while temp_val > 0:
            digits_list.append(temp_val % 10)
            temp_val //= 10

        all_odd_flag: bool = True
        digit_idx: int = 0
        while digit_idx < len(digits_list) and all_odd_flag:
            # digit is odd iff (digit -1) % 2 == 0
            if ((digits_list[digit_idx] - 1) % 2) != 0:
                all_odd_flag = False
            digit_idx += 1

        if all_odd_flag:
            odd_collection.append(current_value)
        idx += 1

    sorted_collection: List[int] = odd_collection
    i: int = 0
    while i < len(sorted_collection) - 1:
        j: int = i + 1
        while j < len(sorted_collection):
            if sorted_collection[i] > sorted_collection[j]:
                temp_swap = sorted_collection[i]
                sorted_collection[i] = sorted_collection[j]
                sorted_collection[j] = temp_swap
            j += 1
        i += 1

    return sorted_collection