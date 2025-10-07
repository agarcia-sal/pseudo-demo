from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        coeff = 1
        if integer_value < 0:
            integer_value = -integer_value
            coeff = -1
        digits_map = [int(x) for x in str(integer_value)]
        digits_map[0] *= coeff  # apply coefficient to the first digit to account for sign
        acc = sum(digits_map)
        return acc

    collector: List[int] = [digits_sum(num) for num in array_of_integers]
    reduced: List[int] = [val for val in collector if val > 0]
    return len(reduced)