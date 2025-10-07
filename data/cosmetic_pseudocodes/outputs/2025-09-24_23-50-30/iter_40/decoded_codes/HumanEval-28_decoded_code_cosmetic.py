from typing import List

def concatenate(array_of_tokens: List[str]) -> str:
    index_tracker: int = 0
    concatenated_string: str = ""
    while index_tracker < len(array_of_tokens):
        concatenated_string += array_of_tokens[index_tracker]
        index_tracker += 1
    return concatenated_string