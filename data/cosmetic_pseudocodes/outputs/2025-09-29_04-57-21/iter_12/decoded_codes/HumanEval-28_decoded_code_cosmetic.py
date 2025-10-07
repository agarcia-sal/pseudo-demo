from typing import List

def concatenate(stack_of_strings: List[str]) -> str:
    output_string: str = ""
    index_counter: int = 0
    while index_counter < len(stack_of_strings):
        output_string += stack_of_strings[index_counter]
        index_counter += 1
    return output_string