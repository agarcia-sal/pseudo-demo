from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        polarity = 1
        if integer_value < 0:
            integer_value = -integer_value
            polarity = -polarity

        digit_chars = str(integer_value)
        digits_list: List[int] = [int(char) for char in digit_chars]

        digits_list[0] *= polarity

        accumulator = 0
        idx = 0
        while idx < len(digits_list):
            accumulator += digits_list[idx]
            idx += 1

        return accumulator

    results: List[int] = []
    ptr = 0
    while ptr < len(array_of_integers):
        results.append(digits_sum(array_of_integers[ptr]))
        ptr += 1

    count_positive = 0
    for val in results:
        if val > 0:
            count_positive += 1

    return count_positive