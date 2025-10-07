from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    accumulator_odd: int = 0
    accumulator_even: int = 0

    def count_odds(index: int) -> None:
        nonlocal accumulator_odd
        if index >= len(list_one):
            return
        if list_one[index] % 2 == 1:
            accumulator_odd += 1
        count_odds(index + 1)

    count_odds(0)

    for idx in range(len(list_two)):
        if list_two[idx] % 2 == 0:
            accumulator_even += 1

    return "YES" if accumulator_odd <= accumulator_even else "NO"