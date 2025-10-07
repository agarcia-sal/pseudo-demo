from typing import List

def exchange(alpha: List[int], beta: List[int]) -> str:
    tally_odd: int = 0
    idx_one: int = 0
    length_one: int = len(alpha)

    while idx_one < length_one:
        if alpha[idx_one] % 2 != 0:
            tally_odd += 1
        idx_one += 1

    tally_even: int = 0
    idx_two: int = 0
    length_two: int = len(beta)

    while True:
        if idx_two >= length_two:
            break
        value = beta[idx_two]
        if not (value % 2 != 0):
            tally_even += 1
        idx_two += 1

    return "YES" if tally_even >= tally_odd else "NO"