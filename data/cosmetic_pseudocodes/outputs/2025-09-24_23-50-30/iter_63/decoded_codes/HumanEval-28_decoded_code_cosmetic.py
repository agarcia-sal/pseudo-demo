from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    index_tracker: int = 0
    accumulated_string: str = ""
    while index_tracker < len(sequence_of_texts):
        accumulated_string += sequence_of_texts[index_tracker]
        index_tracker += 1
    return accumulated_string