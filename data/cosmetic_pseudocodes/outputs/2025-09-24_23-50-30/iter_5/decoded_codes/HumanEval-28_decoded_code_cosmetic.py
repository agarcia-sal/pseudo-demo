from typing import Iterable

def concatenate(buffer: Iterable[str]) -> str:
    accumulator: str = ""
    for element in buffer:
        accumulator += element
    return accumulator