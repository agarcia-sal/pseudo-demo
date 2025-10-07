from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def abs_sum(index: int, acc: int) -> int:
        if index >= len(array_of_integers):
            return acc
        return abs_sum(index + 1, acc + abs(array_of_integers[index]))

    def count_negatives(idx: int, tally: int) -> int:
        if idx == len(array_of_integers):
            return tally
        if array_of_integers[idx] < 0:
            return count_negatives(idx + 1, tally + 1)
        return count_negatives(idx + 1, tally)

    if len(array_of_integers) == 0:
        return None

    zero_flag = False
    iterator = 0
    while iterator < len(array_of_integers) and not zero_flag:
        if array_of_integers[iterator] == 0:
            zero_flag = True
        else:
            iterator += 1

    POWER_NEG_ONE = -1
    signed_multiplier = 0
    if zero_flag:
        signed_multiplier = 0
    else:
        negative_count = count_negatives(0, 0)
        exponent = negative_count
        result = 1
        while exponent > 0:
            result *= POWER_NEG_ONE
            exponent -= 1
        signed_multiplier = result

    magnitude_sum = abs_sum(0, 0)
    return signed_multiplier * magnitude_sum