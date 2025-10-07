from typing import List

def concatenate(array_of_texts: List[str]) -> str:
    combined_output: str = ""
    index_counter: int = 0
    while index_counter < len(array_of_texts):
        current_text: str = array_of_texts[index_counter]
        combined_output += current_text
        index_counter += 1
    return combined_output