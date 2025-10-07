from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign: int = 1
        if number < 0:
            number = -number
            sign = -1
        digits_as_ints: List[int] = [int(d) for d in str(number)]
        if digits_as_ints:
            digits_as_ints[0] *= sign
        return sum(digits_as_ints)

    digit_sums: List[int] = [digits_sum(element) for element in array_of_integers]
    filtered_elements: List[int] = [ds for ds in digit_sums if ds > 0]
    return len(filtered_elements)