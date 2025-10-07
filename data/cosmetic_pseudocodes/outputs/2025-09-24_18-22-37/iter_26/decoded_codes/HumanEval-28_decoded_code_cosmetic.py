from typing import Sequence

def concatenate(alphabet_collection: Sequence[str]) -> str:
    index_counter: int = 0
    resulting_string: str = ""
    while index_counter < len(alphabet_collection):
        current_entry: str = alphabet_collection[index_counter]
        resulting_string += current_entry
        index_counter += 1
    return resulting_string