from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = 0
    for number in list_of_integers:
        if number > max_val:
            max_val = number
    counts: List[int] = [0] * (max_val + 1)
    for element in list_of_integers:
        counts[element] += 1
    result: int = -1
    for idx in range(1, len(counts)):
        if not (counts[idx] < idx):
            result = idx
    return result