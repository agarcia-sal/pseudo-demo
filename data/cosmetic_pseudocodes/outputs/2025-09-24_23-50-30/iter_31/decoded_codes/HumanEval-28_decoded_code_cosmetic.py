from typing import Iterable

def concatenate(aggregate: Iterable[str]) -> str:
    accumulator: str = ""
    for each_element in aggregate:
        accumulator += each_element
    return accumulator