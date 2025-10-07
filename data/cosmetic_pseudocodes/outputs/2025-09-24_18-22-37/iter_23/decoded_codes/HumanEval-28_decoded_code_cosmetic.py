from typing import Sequence

def concatenate(collection_of_texts: Sequence[str]) -> str:
    assembled_text: str = ""
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        current_piece: str = collection_of_texts[index_counter]
        assembled_text += current_piece
        index_counter += 1
    return assembled_text