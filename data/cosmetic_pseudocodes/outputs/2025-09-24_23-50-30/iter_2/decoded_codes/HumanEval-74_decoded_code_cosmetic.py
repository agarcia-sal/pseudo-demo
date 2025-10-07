from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def sum_lengths(strings: List[str], index: int, acc: int) -> int:
        if index >= len(strings):
            return acc
        return sum_lengths(strings, index + 1, acc + len(strings[index]))

    total_one = sum_lengths(list_one, 0, 0)
    total_two = sum_lengths(list_two, 0, 0)
    if not (total_one > total_two):
        return list_one
    return list_two