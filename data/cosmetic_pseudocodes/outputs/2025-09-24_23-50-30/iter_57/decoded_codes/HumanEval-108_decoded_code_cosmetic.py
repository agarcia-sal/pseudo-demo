from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        neg_factor = 1
        while integer_value < 0:
            integer_value = -integer_value
            neg_factor = -1
        digits_string = str(integer_value)
        digits_collection: List[int] = []
        idx = 0
        while idx < len(digits_string):
            digits_collection.append(int(digits_string[idx]))
            idx += 1
        digits_collection[0] *= neg_factor
        sum_accumulator = 0
        for digit_value in digits_collection:
            sum_accumulator += digit_value
        return sum_accumulator

    sum_results: List[int] = []
    pos1 = 0
    while pos1 < len(array_of_integers):
        current_value = array_of_integers[pos1]
        sum_results.append(digits_sum(current_value))
        pos1 += 1

    positive_filter: List[int] = []
    pos2 = 0
    while pos2 < len(sum_results):
        if not (sum_results[pos2] <= 0):
            positive_filter.append(sum_results[pos2])
        pos2 += 1

    return len(positive_filter)