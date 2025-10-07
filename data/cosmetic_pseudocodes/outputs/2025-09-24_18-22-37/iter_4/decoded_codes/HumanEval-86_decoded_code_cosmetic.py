from typing import List

def anti_shuffle(original_text: str) -> str:
    words_array: List[str] = original_text.split(" ")
    sorted_words_collection: List[str] = []
    idx: int = 0
    while idx < len(words_array):
        current_word: str = words_array[idx]
        char_array: List[str] = sorted(current_word)
        recombined_word: str = "".join(char_array)
        sorted_words_collection.append(recombined_word)
        idx += 1
    output_text: str = ""
    i: int = 0
    while i < len(sorted_words_collection):
        if i == len(sorted_words_collection) - 1:
            output_text += sorted_words_collection[i]
        else:
            output_text += sorted_words_collection[i] + " "
        i += 1
    return output_text