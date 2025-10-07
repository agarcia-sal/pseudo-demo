from typing import Iterable

def concatenate(strings: Iterable[str]) -> str:
    result: str = ""
    for s in strings:
        result += s
    return result