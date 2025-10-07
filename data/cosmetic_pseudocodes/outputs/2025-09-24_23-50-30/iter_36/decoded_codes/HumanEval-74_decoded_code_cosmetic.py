from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def accumulate_length(collection: List[str], index: int, accumulated: int) -> int:
        if index >= len(collection):
            return accumulated
        return accumulate_length(collection, index + 1, accumulated + len(collection[index]))

    sum_one = accumulate_length(list_one, 0, 0)
    sum_two = accumulate_length(list_two, 0, 0)

    if not (sum_one > sum_two):
        return list_one
    return list_two