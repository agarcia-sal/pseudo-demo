from typing import Iterable

def concatenate(collection_of_strings: Iterable[str]) -> str:
    result_string: str = ""
    index: int = 0
    collection_list = list(collection_of_strings)
    while index < len(collection_list):
        result_string += collection_list[index]
        index += 1
    return result_string