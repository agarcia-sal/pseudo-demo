from functools import reduce
from typing import Set


def fizz_buzz(integer_n: int) -> int:
    def gather_multiples(current_index: int, collected_set: Set[int]) -> Set[int]:
        if current_index >= integer_n:
            return collected_set
        if current_index % 11 == 0 or current_index % 13 == 0:
            collected_set.add(current_index)
        return gather_multiples(current_index + 1, collected_set)

    multiples_set: Set[int] = gather_multiples(0, set())
    # Convert set to list to have fixed traversal order for reduce
    multiples_list = list(multiples_set)
    merged_string = reduce(lambda acc, val: acc + str(val), multiples_list, "")
    accumulator = 0
    index_counter = 0
    while index_counter < len(merged_string):
        if merged_string[index_counter] == '7':
            accumulator += 1
        index_counter += 1
    return accumulator