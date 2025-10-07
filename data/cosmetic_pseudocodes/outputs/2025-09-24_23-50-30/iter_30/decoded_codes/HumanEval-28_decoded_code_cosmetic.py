from typing import Sequence

def concatenate(sequences: Sequence[str]) -> str:
    index: int = 0
    result: str = ""
    while index < len(sequences):
        result += sequences[index]
        index += 1
    return result