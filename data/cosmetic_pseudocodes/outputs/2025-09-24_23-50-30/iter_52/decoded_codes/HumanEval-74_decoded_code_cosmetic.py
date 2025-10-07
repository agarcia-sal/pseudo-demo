from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:

    def accumulate_lengths(collection: List[str]) -> int:

        def helper(index: int, sum_so_far: int) -> int:
            if index == len(collection):
                return sum_so_far
            else:
                return helper(index + 1, sum_so_far + len(collection[index]))

        return helper(0, 0)

    total_length_one = accumulate_lengths(list_one)
    total_length_two = accumulate_lengths(list_two)

    if total_length_one <= total_length_two:
        return list_one
    else:
        return list_two