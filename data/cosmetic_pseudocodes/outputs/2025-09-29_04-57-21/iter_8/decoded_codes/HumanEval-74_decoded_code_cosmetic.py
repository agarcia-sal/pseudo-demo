from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    iterator_one = iter(list_one)
    while True:
        try:
            current_str = next(iterator_one)
            sum_one += len(current_str)
        except StopIteration:
            break

    sum_two: int = 0
    iterator_two = iter(list_two)
    while True:
        try:
            current_str_two = next(iterator_two)
            sum_two += len(current_str_two)
        except StopIteration:
            break

    if not (sum_one > sum_two):
        return list_one
    return list_two