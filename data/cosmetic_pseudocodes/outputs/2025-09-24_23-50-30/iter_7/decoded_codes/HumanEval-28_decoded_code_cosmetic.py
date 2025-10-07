from typing import Iterable

def concatenate(string_collection: Iterable[str]) -> str:
    accumulator: str = ""
    for element in string_collection:
        accumulator += element
    return accumulator