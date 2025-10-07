from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    zeta: int = 0
    xi: int = 0

    def traverse_odd(index: int) -> None:
        nonlocal zeta
        if index >= len(array_alpha):
            return
        if array_alpha[index] % 2 == 1:
            zeta += 1
        traverse_odd(index + 1)

    def traverse_even(index: int) -> None:
        nonlocal xi
        if index >= len(array_beta):
            return
        if array_beta[index] % 2 == 0:
            xi += 1
        traverse_even(index + 1)

    traverse_odd(0)
    traverse_even(0)

    return "YES" if xi >= zeta else "NO"