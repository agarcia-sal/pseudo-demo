from typing import Iterable

def concatenate(inputs: Iterable[str]) -> str:
    combined_string = ""
    for element in inputs:
        combined_string += element
    return combined_string