from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    cumulative_length_first: int = 0
    iterator_first = iter(list_one)
    while True:
        try:
            current_string = next(iterator_first)
            cumulative_length_first += len(current_string)
        except StopIteration:
            break

    cumulative_length_second: int = 0
    iterator_second = iter(list_two)
    while True:
        try:
            current_string_alt = next(iterator_second)
            cumulative_length_second += len(current_string_alt)
        except StopIteration:
            break

    if not (cumulative_length_first > cumulative_length_second):
        return list_one
    return list_two