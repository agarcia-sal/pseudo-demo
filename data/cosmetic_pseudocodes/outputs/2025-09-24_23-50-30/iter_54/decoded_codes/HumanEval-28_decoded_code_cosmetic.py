from typing import Sequence

def concatenate(sequence_strings: Sequence[str]) -> str:
    index_position: int = 0
    result_builder: str = ""
    while index_position < len(sequence_strings):
        result_builder += sequence_strings[index_position]
        index_position += 1
    return result_builder