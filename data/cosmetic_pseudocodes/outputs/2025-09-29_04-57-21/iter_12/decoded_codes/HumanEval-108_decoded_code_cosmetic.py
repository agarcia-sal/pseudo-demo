from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1
        digits_chars = str(integer_value)
        digits_array: List[int] = []
        index_counter = 0
        while index_counter < len(digits_chars):
            digits_array.append(int(digits_chars[index_counter]))
            index_counter += 1
        digits_array[0] *= multiplier_sign
        total_digits_sum = 0
        for digit_value in digits_array:
            total_digits_sum += digit_value
        return total_digits_sum

    sums_collection: List[int] = []
    pos = 0
    while pos < len(array_of_integers):
        current_num = array_of_integers[pos]
        calculated_sum = digits_sum(current_num)
        sums_collection.append(calculated_sum)
        pos += 1

    positive_sums: List[int] = []
    idx = 0
    while idx < len(sums_collection):
        candidate_value = sums_collection[idx]
        if candidate_value > 0:
            positive_sums.append(candidate_value)
        idx += 1

    return len(positive_sums)