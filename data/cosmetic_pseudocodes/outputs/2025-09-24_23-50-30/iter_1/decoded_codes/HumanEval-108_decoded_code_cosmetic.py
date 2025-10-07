from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign = -1

        digits: List[int] = [int(ch) for ch in str(integer_value)]
        if digits:
            digits[0] *= sign

        total: int = sum(digits)
        return total

    sums_list: List[int] = []
    idx: int = 0
    while idx < len(array_of_integers):
        sums_list.append(digits_sum(array_of_integers[idx]))
        idx += 1

    positive_sums: List[int] = [val for val in sums_list if val > 0]
    return len(positive_sums)