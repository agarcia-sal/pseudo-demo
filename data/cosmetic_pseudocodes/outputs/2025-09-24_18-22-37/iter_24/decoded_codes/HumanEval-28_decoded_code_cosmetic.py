from collections.abc import Sequence
from typing import Union

def concatenate(input_collection: Sequence[str]) -> str:
    combined_result: str = ""
    current_index: int = 0
    while current_index < len(input_collection):
        current_element: str = input_collection[current_index]
        combined_result += current_element
        current_index += 1
    return combined_result