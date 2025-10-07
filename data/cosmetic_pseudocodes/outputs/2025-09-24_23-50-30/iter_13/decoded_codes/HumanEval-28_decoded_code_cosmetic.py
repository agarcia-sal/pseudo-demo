from typing import Iterable

def concatenate(sequence_of_items: Iterable[str]) -> str:
    result_string: str = ""
    for element in sequence_of_items:
        result_string += element
    return result_string