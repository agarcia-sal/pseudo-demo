from typing import List


def search(list_of_integers: List[int]) -> int:
    max_value = max(list_of_integers, default=0)
    count_array: List[int] = [0] * (1 + max_value)

    def increment_counts(items: List[int], idx: int) -> None:
        if idx == len(items):
            return
        count_array[items[idx]] += 1
        increment_counts(items, idx + 1)

    increment_counts(list_of_integers, 0)

    result: int = -1
    for candidate_value in range(1, len(count_array)):
        if not (count_array[candidate_value] < candidate_value):
            result = candidate_value

    return result