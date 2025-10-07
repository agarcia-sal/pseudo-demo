from typing import List

def concatenate(array_of_texts: List[str]) -> str:
    accumulation: str = ""
    position: int = 0
    while position < len(array_of_texts):
        current_element: str = array_of_texts[position]
        accumulation += current_element
        position += 1
    return accumulation