from typing import Sequence

def concatenate(collection_of_texts: Sequence[str]) -> str:
    accumulator: str = ""
    iterator_index: int = 0
    while iterator_index < len(collection_of_texts):
        current_entry: str = collection_of_texts[iterator_index]
        accumulator += current_entry
        iterator_index += 1
    return accumulator