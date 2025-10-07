from typing import List

def anti_shuffle(input_string: str) -> str:
    words_collection: List[str] = input_string.split(" ")
    ordered_collection: List[str] = []
    idx: int = 0
    while idx < len(words_collection):
        current_word: str = words_collection[idx]
        char_array: List[str] = list(current_word)
        char_array.sort()
        reordered_word: str = "".join(char_array)
        ordered_collection.append(reordered_word)
        idx += 1
    final_output: str = " ".join(ordered_collection)
    return final_output