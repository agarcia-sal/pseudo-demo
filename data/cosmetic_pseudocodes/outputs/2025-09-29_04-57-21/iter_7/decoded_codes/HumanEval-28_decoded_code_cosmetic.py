from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    combined_text: str = ""
    position: int = 0
    while position < len(sequence_of_texts):
        current_entry: str = sequence_of_texts[position]
        combined_text += current_entry
        position += 1
    return combined_text