from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result_string: str = ""
    index_counter: int = 0
    total_items: int = len(list_of_strings)
    while index_counter < total_items:
        current_element: str = list_of_strings[index_counter]
        temp_string: str = result_string + current_element
        result_string = temp_string
        index_counter += 1
    return result_string