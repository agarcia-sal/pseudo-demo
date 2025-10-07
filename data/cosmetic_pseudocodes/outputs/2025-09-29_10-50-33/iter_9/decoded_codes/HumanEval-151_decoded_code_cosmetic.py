from typing import List


def double_the_difference(list_of_numbers: List[int]) -> int:
    index_counter: int = 1
    aggregate_sum: int = 0

    while index_counter <= len(list_of_numbers):
        candidate: int = list_of_numbers[index_counter - 1]
        if candidate > 0 and candidate % 2 != 0 and "." not in str(candidate):
            aggregate_sum += candidate * candidate
        index_counter += 1

    return aggregate_sum