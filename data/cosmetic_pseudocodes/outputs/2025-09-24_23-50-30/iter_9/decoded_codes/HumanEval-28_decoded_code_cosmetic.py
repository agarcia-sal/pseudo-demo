from typing import Sequence

def concatenate(sequence_of_strings: Sequence[str]) -> str:
    result: str = ""
    for element in sequence_of_strings:
        result += element
    return result