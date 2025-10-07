from typing import Sequence

def concatenate(sequence_of_strings: Sequence[str]) -> str:
    accumulator: str = ""
    for element in sequence_of_strings:
        accumulator += element
    return accumulator