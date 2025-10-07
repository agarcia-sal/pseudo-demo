from typing import Iterable

def concatenate(collection_of_texts: Iterable[str]) -> str:
    accumulator: str = ""
    for text_element in collection_of_texts:
        accumulator += text_element
    return accumulator