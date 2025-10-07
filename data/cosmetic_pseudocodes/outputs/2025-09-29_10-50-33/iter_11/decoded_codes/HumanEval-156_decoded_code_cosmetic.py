from typing import List


def int_to_mini_roman(amount: int) -> str:
    values: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    indexer: int = 0
    accumulator: str = ""

    while amount > 0 and indexer < len(values):
        if values[indexer] <= amount:
            counts: int = amount // values[indexer]
            amount -= counts * values[indexer]
            accumulator += symbols[indexer] * counts
        else:
            indexer += 1

    output: str = "".join(ch.lower() for ch in accumulator)
    return output