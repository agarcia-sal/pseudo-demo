from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    merged_string: str = ""
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        merged_string += list_of_strings[index_counter]
        index_counter += 1
    return merged_string