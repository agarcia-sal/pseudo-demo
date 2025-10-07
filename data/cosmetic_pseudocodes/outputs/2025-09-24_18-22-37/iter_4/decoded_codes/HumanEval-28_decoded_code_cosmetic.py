from typing import List

def concatenate(input_list: List[str]) -> str:
    index: int = 0
    final_string: str = ""
    while index < len(input_list):
        final_string += input_list[index]
        index += 1
    return final_string