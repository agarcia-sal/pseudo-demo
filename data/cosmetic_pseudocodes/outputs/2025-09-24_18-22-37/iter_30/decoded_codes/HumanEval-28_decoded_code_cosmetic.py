from typing import Sequence

def concatenate(strings_collection: Sequence[str]) -> str:
    combined_string: str = ""
    current_idx: int = 0
    while current_idx < len(strings_collection):
        element: str = strings_collection[current_idx]
        combined_string += element
        current_idx += 1
    return combined_string