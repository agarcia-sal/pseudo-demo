from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_collection: List[str] = []
    index: int = 0
    while index < len(words_array):
        current_word: str = words_array[index]
        characters_array: List[str] = list(current_word)
        characters_array.sort()
        new_word: str = "".join(characters_array)
        sorted_words_collection.append(new_word)
        index += 1
    final_output: str = " ".join(sorted_words_collection)
    return final_output