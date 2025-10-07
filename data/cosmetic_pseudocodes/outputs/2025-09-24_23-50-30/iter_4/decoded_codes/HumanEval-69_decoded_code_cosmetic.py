from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_val = max(list_of_integers)
    count_map: List[int] = [0] * (max_val + 1)

    def increment_counts(idx: int) -> None:
        if idx > len(list_of_integers):
            return
        count_map[list_of_integers[idx - 1]] += 1
        increment_counts(idx + 1)

    increment_counts(1)
    answer: int = -1
    index: int = len(count_map) - 1
    while index >= 1:
        if count_map[index] >= index:
            answer = index
            break
        index -= 1
    return answer