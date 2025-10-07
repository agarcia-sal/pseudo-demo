from typing import Iterable

def concatenate(collection_of_texts: Iterable[str]) -> str:
    accumulator: str = ""
    index: int = 0
    texts_list = list(collection_of_texts)  # convert to list for indexing
    while index < len(texts_list):
        accumulator += texts_list[index]
        index += 1
    return accumulator