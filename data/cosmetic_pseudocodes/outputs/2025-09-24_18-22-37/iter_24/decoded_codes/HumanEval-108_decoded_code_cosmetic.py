from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        flag_sign: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            flag_sign = -1
        digit_strings: str = str(integer_value)
        digit_collection: List[int] = [int(ch) for ch in digit_strings]
        digit_collection[0] *= flag_sign
        sum_accumulator: int = sum(digit_collection)
        return sum_accumulator

    result_collector: List[int] = []
    for current_elem in array_of_integers:
        sum_digit = digits_sum(current_elem)
        result_collector.append(sum_digit)

    filtered_collection: List[int] = [candidate_elem for candidate_elem in result_collector if candidate_elem > 0]

    return len(filtered_collection)