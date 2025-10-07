from typing import Sequence

def concatenate(container_of_sequences: Sequence[str]) -> str:
    accumulator: str = ""
    index: int = 0
    while index < len(container_of_sequences):
        accumulator += container_of_sequences[index]
        index += 1
    return accumulator