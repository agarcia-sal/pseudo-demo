from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value >= 0:
            abs_integer = integer_value
            head_sign = 1
        else:
            abs_integer = -integer_value
            head_sign = -1

        str_representation = str(abs_integer)
        digits_array: List[int] = [int(ch) for ch in str_representation]

        digits_array[0] *= head_sign

        total = sum(digits_array)
        return total

    results: List[int] = [digits_sum(x) for x in array_of_integers]
    positives: List[int] = [x for x in results if x > 0]

    return len(positives)