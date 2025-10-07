from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result_string = ""
    iterator = iter(list_of_strings)
    while True:
        try:
            current_element = next(iterator)
            result_string += current_element
        except StopIteration:
            break
    return result_string