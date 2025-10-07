from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        factor_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            factor_sign = -1
        digits_collection = [int(ch) for ch in str(integer_value)]
        digits_collection[0] *= factor_sign
        accumulator_total = 0
        for idx in range(len(digits_collection)):
            accumulator_total += digits_collection[idx]
        return accumulator_total

    intermediate_results: List[int] = []
    for iterator_idx in range(len(array_of_integers)):
        current_item = array_of_integers[iterator_idx]
        intermediate_results.append(digits_sum(current_item))

    positive_items: List[int] = []
    for pos_idx in range(len(intermediate_results)):
        candidate = intermediate_results[pos_idx]
        if candidate > 0:
            positive_items.append(candidate)

    return len(positive_items)