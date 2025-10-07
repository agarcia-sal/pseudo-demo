from typing import Iterable

def concatenate(array_of_texts: Iterable[str]) -> str:
    combined_text: str = ""
    for single_text in array_of_texts:
        combined_text += single_text
    return combined_text