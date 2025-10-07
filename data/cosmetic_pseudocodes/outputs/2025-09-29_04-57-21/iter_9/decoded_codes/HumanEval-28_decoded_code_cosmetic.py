from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    combined_text: str = ""
    index_counter: int = 0

    while index_counter < len(list_of_strings):
        current_segment: str = list_of_strings[index_counter]
        combined_text += current_segment
        index_counter += 1

    return combined_text