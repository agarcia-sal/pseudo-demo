from typing import Sequence

def concatenate(array_of_texts: Sequence[str]) -> str:
    combined_text: str = ""
    position: int = 1
    length: int = len(array_of_texts)
    while position <= length:
        combined_text += array_of_texts[position - 1]  # Adjust for 0-based indexing
        position += 1
    return combined_text