from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_array: List[str] = []
    for word_element in words_array:
        characters_array: List[str] = list(word_element)
        characters_array.sort()
        sorted_word_string: str = "".join(characters_array)
        sorted_words_array.append(sorted_word_string)
    final_output: str = " ".join(sorted_words_array)
    return final_output