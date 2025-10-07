from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        delta: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            delta = -delta

        str_digits = str(integer_value)
        digit_collection: List[int] = [int(ch) for ch in str_digits]

        digit_collection[0] *= delta

        accumulator: int = 0
        pointer: int = 0
        while pointer < len(digit_collection):
            accumulator += digit_collection[pointer]
            pointer += 1

        return accumulator

    results: List[int] = []
    pos: int = 0
    while pos < len(array_of_integers):
        current_element = array_of_integers[pos]
        results.append(digits_sum(current_element))
        pos += 1

    count_positive: int = 0
    for item in results:
        if item > 0:
            count_positive += 1

    return count_positive