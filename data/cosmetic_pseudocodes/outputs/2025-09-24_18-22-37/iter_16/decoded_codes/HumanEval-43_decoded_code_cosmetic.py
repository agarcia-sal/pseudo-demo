from typing import List


def pairs_sum_to_zero(numbers_list: List[int]) -> bool:
    outer_length: int = len(numbers_list)
    counter_one: int = 0
    while counter_one < outer_length:
        value_one: int = numbers_list[counter_one]
        counter_two: int = counter_one + 1
        while counter_two < outer_length:
            value_two: int = numbers_list[counter_two]
            total_sum: int = value_one + value_two
            if total_sum == 0:
                return True
            counter_two += 1
        counter_one += 1
    return False