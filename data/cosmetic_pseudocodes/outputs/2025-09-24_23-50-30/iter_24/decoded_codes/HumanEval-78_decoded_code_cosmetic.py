from typing import List


def hex_key(alpha: str) -> int:
    prime_collection: List[str] = ['B', '2', '3', '7', 'D', '5']
    accumulator: int = 0

    def count_chars(beta: str, gamma: int) -> None:
        nonlocal accumulator
        if gamma > len(beta) - 1:
            return
        if beta[gamma] in prime_collection:
            accumulator += 1
        count_chars(beta, gamma + 1)

    count_chars(alpha, 0)
    return accumulator