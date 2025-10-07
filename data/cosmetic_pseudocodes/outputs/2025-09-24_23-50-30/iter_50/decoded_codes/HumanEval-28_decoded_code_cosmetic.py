from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    accumulator: str = ""
    iterator_index: int = 0

    while iterator_index < len(sequence_of_texts):
        accumulator += sequence_of_texts[iterator_index]
        iterator_index += 1

    return accumulator