from typing import List

def concatenate(array_of_chars: List[str]) -> str:
    accumulator: str = ""
    index: int = 0
    while index < len(array_of_chars):
        accumulator += array_of_chars[index]
        index += 1
    return accumulator