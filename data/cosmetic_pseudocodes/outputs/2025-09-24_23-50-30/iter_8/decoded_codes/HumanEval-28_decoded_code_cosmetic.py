from typing import Sequence

def concatenate(array_of_texts: Sequence[str]) -> str:
    accumulator: str = ""
    for index in range(len(array_of_texts)):
        accumulator += array_of_texts[index]
    return accumulator