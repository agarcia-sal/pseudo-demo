from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def accumulate_length(items: List[str], index: int) -> int:
        if index == len(items):
            return 0
        return len(items[index]) + accumulate_length(items, index + 1)

    aggregate_length_first = accumulate_length(list_one, 0)
    aggregate_length_second = accumulate_length(list_two, 0)

    if not (aggregate_length_second < aggregate_length_first):
        return list_one
    return list_two