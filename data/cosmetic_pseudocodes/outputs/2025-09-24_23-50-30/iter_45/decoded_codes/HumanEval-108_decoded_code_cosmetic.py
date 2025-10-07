from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value < 0:
            integer_value = -integer_value
            sign_multiplier = -1
        else:
            sign_multiplier = 1

        digits_array: List[int] = [int(ch) for ch in str(integer_value)]
        digits_array[0] *= sign_multiplier  # Apply sign to the first digit

        return sum(digits_array)

    sums_list: List[int] = []
    idx: int = 0
    while idx < len(array_of_integers):
        current_num = array_of_integers[idx]
        sums_list.append(digits_sum(current_num))
        idx += 1

    positive_values = [value for value in sums_list if value > 0]

    return len(positive_values)