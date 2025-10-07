from typing import Iterable

def concatenate(sequence_of_segments: Iterable[str]) -> str:
    accumulator: str = ""
    for element in sequence_of_segments:
        accumulator += element
    return accumulator