from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    combined_text: str = ""
    for text_element in list_of_strings:
        combined_text += text_element
    return combined_text