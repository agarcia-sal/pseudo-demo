from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    result_string: str = ""
    for element in sequence_of_texts:
        result_string += element
    return result_string