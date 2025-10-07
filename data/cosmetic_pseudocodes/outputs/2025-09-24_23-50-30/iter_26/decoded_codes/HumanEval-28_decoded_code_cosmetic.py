from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    index: int = 0
    result_text: str = ""

    while index < len(sequence_of_texts):
        result_text += sequence_of_texts[index]
        index += 1

    return result_text