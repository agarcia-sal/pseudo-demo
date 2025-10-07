from typing import Iterable

def exchange(alpha: Iterable[int], beta: Iterable[int]) -> str:
    x: int = 0
    y: int = 0
    for value in alpha:
        if (value - 2 * (value // 2)) == 1:
            x += 1
    for item in beta:
        if not ((item - 2 * (item // 2)) == 1):
            y += 1
    return "YES" if y >= x else "NO"