from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        digits_list = [int(char) for char in str(integer_value)]
        digits_list[0] *= multiplier_sign

        total_sum = sum(digits_list)
        return total_sum

    sums_collection: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        current_num = array_of_integers[idx]
        sum_digits = digits_sum(current_num)
        sums_collection += [sum_digits]
        idx += 1

    filtered_items: List[int] = []
    for item in sums_collection:
        if item > 0:
            filtered_items += [item]

    return len(filtered_items)