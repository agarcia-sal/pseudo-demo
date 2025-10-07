from typing import List

def concatenate(array_of_texts: List[str]) -> str:
    merged_text: str = ""
    idx: int = 0
    while idx < len(array_of_texts):
        merged_text += array_of_texts[idx]
        idx += 1
    return merged_text