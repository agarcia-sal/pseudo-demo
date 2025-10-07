from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    def count_odds(idx: int) -> None:
        nonlocal tally_odd
        if idx < len(array_alpha):
            if array_alpha[idx] % 2 == 1:
                tally_odd += 1
            count_odds(idx + 1)

    def count_evens(idx: int) -> None:
        nonlocal tally_even
        if idx < len(array_beta):
            if array_beta[idx] % 2 == 0:
                tally_even += 1
            count_evens(idx + 1)

    count_odds(0)
    count_evens(0)

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"