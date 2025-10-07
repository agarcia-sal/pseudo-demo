from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_input: int) -> int:
        multiplier_sign = 1
        if integer_input < 0:
            integer_input = -integer_input
            multiplier_sign = -1
        digits_list: List[int] = [int(d) for d in str(integer_input)]
        digits_list[0] *= multiplier_sign
        total_sum = 0
        for digit in digits_list:
            total_sum += digit
        return total_sum

    def map_to_sums(index: int, acc: List[int], input_array: List[int]) -> List[int]:
        if index >= len(input_array):
            return acc
        return map_to_sums(index + 1, acc + [digits_sum(input_array[index])], input_array)

    digit_sums_list = map_to_sums(0, [], array_of_integers)

    def filter_positive(list_to_filter: List[int], idx: int, collector: List[int]) -> List[int]:
        if idx >= len(list_to_filter):
            return collector
        if list_to_filter[idx] > 0:
            return filter_positive(list_to_filter, idx + 1, collector + [list_to_filter[idx]])
        else:
            return filter_positive(list_to_filter, idx + 1, collector)

    positives_list = filter_positive(digit_sums_list, 0, [])

    return len(positives_list)