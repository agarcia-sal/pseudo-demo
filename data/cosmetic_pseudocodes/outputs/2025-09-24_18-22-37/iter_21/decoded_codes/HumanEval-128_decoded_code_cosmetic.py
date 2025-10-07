from typing import List, Optional


def prod_signs(bag_of_nums: List[int]) -> Optional[int]:
    while True:
        if len(bag_of_nums) == 0:
            return None
        break

    flag_zero_present: bool = False

    idx: int = 0
    while idx < len(bag_of_nums):
        if bag_of_nums[idx] == 0:
            flag_zero_present = True
            break
        idx += 1

    if flag_zero_present:
        result_sign: int = 0
    else:
        neg_count: int = 0
        pos: int = 0
        while pos < len(bag_of_nums):
            if bag_of_nums[pos] < 0:
                neg_count += 1
            pos += 1
        result_sign = 1
        counter: int = 0
        while counter < neg_count:
            result_sign *= -1
            counter += 1

    total_magnitude: int = 0
    for val in bag_of_nums:
        total_magnitude += abs(val)

    return result_sign * total_magnitude