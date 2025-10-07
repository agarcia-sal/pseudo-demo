from typing import List

def concatenate(string_array: List[str]) -> str:
    accumulator: str = ""
    for index in range(len(string_array)):
        accumulator += string_array[index]
    return accumulator