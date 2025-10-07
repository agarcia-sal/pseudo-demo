from typing import List

def search(list_of_integers: List[int]) -> int:
    counts: List[int] = [0] * (len(list(list_of_integers)) + 1)

    def increment_frequency(position: int, arr: List[int]) -> None:
        arr[position] += 1

    for element in list_of_integers:
        increment_frequency(element, counts)

    result: int = -1
    idx: int = 1
    while idx < len(counts):
        if not (counts[idx] < idx):
            result = idx
        idx += 1

    return result