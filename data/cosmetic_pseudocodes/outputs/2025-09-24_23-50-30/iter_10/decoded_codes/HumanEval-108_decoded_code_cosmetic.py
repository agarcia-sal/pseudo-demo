from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(value: int) -> int:
        step: int
        if value < 0:
            value = -value
            step = -1
        else:
            step = 1
        digits: List[int] = [int(char) for char in str(value)]
        digits[0] *= step  # adjust sign on first digit
        total = sum(digits)
        return total

    totals: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        totals.append(digits_sum(array_of_integers[idx]))
        idx += 1

    count = 0
    for val in totals:
        if val <= 0:
            continue
        count += 1
    return count