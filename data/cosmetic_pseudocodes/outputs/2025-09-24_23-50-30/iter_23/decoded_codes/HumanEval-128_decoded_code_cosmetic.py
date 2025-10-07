from typing import List, Optional


def prod_signs(list_of_nums: List[int]) -> Optional[int]:
    if not list_of_nums:
        return None

    if any(element == 0 for element in list_of_nums):
        result_sign: int = 0
    else:
        negatives_count = sum(1 for x in list_of_nums if x < 0)
        result_sign = 1
        for _ in range(negatives_count):
            result_sign *= -1

    magnitudes_total = sum(abs(number) for number in list_of_nums)
    return result_sign * magnitudes_total