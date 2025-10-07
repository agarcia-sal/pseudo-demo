from typing import Sequence

def concatenate(fragments: Sequence[str]) -> str:
    accumulated = ""
    for index in range(1, len(fragments) + 1):
        accumulated += fragments[index - 1]
    return accumulated