from typing import Set


def hex_key(value: str) -> int:
    primeSymbols: Set[str] = {'2', '3', '5', '7', 'B', 'D'}
    count: int = 0
    pos: int = 0

    while pos < len(value):
        if value[pos] in primeSymbols:
            count += 1
        pos += 1

    return count