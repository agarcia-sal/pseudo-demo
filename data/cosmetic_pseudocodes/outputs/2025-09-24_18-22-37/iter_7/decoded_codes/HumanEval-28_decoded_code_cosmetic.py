from typing import Sequence

def concatenate(collection_of_texts: Sequence[str]) -> str:
    accumulated_text = ""
    position_index = 0
    while position_index < len(collection_of_texts):
        current_element = collection_of_texts[position_index]
        accumulated_text += current_element
        position_index += 1
    return accumulated_text