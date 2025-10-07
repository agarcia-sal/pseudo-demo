from typing import List

def concatenate(array_of_texts: List[str]) -> str:
    result_text: str = ""
    position_index: int = 0
    while position_index < len(array_of_texts):
        result_text += array_of_texts[position_index]
        position_index += 1
    return result_text