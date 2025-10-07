from typing import Sequence

def exchange(collection_alpha: Sequence[int], collection_beta: Sequence[int]) -> str:
    counterA: int = 0
    counterB: int = 0

    def computeOdds(index: int) -> None:
        nonlocal counterA
        if index == len(collection_alpha):
            return
        if ((collection_alpha[index] - 1) % 2) == 0:
            counterA += 1
        computeOdds(index + 1)

    def computeEvens(index: int) -> None:
        nonlocal counterB
        if index == len(collection_beta):
            return
        if (collection_beta[index] % 2) == 0:
            counterB += 1
        computeEvens(index + 1)

    computeOdds(0)
    computeEvens(0)

    if not (counterB < counterA):
        return "YES"
    else:
        return "NO"