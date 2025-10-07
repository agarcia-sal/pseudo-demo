from typing import Sequence

def concatenate(array_of_texts: Sequence[str]) -> str:
    index_counter: int = 1
    combined_text: str = ""
    while index_counter <= len(array_of_texts):
        current_string: str = array_of_texts[index_counter]
        combined_text += current_string
        index_counter += 1
    return combined_text