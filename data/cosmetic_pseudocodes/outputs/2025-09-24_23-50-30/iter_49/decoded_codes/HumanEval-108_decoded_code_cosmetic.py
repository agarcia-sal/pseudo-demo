from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        delta: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            delta = -delta

        def decompose_digits(accumulator: int, position: int) -> int:
            str_val = str(integer_value)
            if position == len(str_val):
                return accumulator
            char_code = str_val[position]
            digit_value = int(char_code)
            adjusted_digit = digit_value
            if position == 0:
                adjusted_digit = digit_value * delta
            return decompose_digits(accumulator + adjusted_digit, position + 1)

        return decompose_digits(0, 0)

    def collect_sums(idx: int, result_list: List[int]) -> List[int]:
        if idx == len(array_of_integers):
            return result_list
        return collect_sums(idx + 1, result_list + [digits_sum(array_of_integers[idx])])

    sums_collection = collect_sums(0, [])

    def count_positive(values: List[int], position: int, counter: int) -> int:
        if position >= len(values):
            return counter
        if values[position] > 0:
            return count_positive(values, position + 1, counter + 1)
        return count_positive(values, position + 1, counter)

    return count_positive(sums_collection, 0, 0)