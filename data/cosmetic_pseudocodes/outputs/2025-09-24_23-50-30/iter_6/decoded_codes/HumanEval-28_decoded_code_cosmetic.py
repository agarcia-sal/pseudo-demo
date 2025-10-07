from typing import Collection

def concatenate(strings_collection: Collection[str]) -> str:
    merged_string: str = ""
    index_counter: int = 0
    while index_counter < len(strings_collection):
        merged_string += strings_collection[index_counter]
        index_counter += 1
    return merged_string