from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    aggregate_string: str = ""
    pos: int = 0
    while pos < len(list_of_strings):
        aggregate_string += list_of_strings[pos]
        pos += 1
    return aggregate_string