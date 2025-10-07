from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        p = 1
        if integer_value < 0:
            integer_value = -integer_value
            p = -1
        digits_list: List[int] = [int(ch) for ch in str(integer_value)]
        digits_list[0] *= p
        total_sum = sum(digits_list)
        return total_sum

    sums_accumulator: List[int] = []
    n = 0
    while n < len(array_of_integers):
        sums_accumulator.append(digits_sum(array_of_integers[n]))
        n += 1

    result_counter = 0
    for v in sums_accumulator:
        if v > 0:
            result_counter += 1

    return result_counter