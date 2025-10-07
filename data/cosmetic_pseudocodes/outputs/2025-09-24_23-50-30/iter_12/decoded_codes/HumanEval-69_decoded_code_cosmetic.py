from typing import List

def search(list_of_integers: List[int]) -> int:
    max_element = max(list_of_integers) if list_of_integers else 0
    frequency_map: List[int] = [0] * (max_element + 1)

    def tally_frequencies(idx: int) -> None:
        if idx == len(list_of_integers):
            return
        frequency_map[list_of_integers[idx]] += 1
        tally_frequencies(idx + 1)

    tally_frequencies(0)
    outcome: int = -1
    current: int = len(frequency_map) - 1
    while current > 0:
        if frequency_map[current] >= current:
            outcome = current
        current -= 1
    return outcome