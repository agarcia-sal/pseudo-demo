from typing import Iterable

def concatenate(collection_of_strs: Iterable[str]) -> str:
    temp_result = ""
    for item in collection_of_strs:
        temp_result += item
    return temp_result