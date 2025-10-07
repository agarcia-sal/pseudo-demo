from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    accumulator: str = ""
    for elementVar in list_of_strings:
        accumulator += elementVar
    return accumulator