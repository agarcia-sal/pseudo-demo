from typing import Iterable

def concatenate(sequence_of_strings: Iterable[str]) -> str:
    result = ""
    for element in sequence_of_strings:
        result += element
    return result