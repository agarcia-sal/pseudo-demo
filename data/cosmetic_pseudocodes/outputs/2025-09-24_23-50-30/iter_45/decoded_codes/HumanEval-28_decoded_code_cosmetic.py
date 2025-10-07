from typing import Iterable

def concatenate(string_collection: Iterable[str]) -> str:
    accumulator: str = ""
    for index in range(len(list(string_collection))):
        accumulator += list(string_collection)[index]
    return accumulator