from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    accumulator: str = ""
    for element in sequence_of_texts:
        accumulator += element
    return accumulator