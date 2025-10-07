from typing import Iterable

def same_chars(alpha: Iterable[str], beta: Iterable[str]) -> bool:
    accumulator = set(alpha)
    collector = set(beta)
    return accumulator == collector