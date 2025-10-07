from typing import Iterable

def concatenate(strings_collection: Iterable[str]) -> str:
    result_string = ""
    for element in strings_collection:
        result_string += element
    return result_string