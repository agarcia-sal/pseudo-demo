from typing import List

def concatenate(array_of_words: List[str]) -> str:
    merged_result: str = ""
    idx: int = 0
    while idx < len(array_of_words):
        current_word: str = array_of_words[idx]
        merged_result += current_word
        idx += 1
    return merged_result