from typing import List

def anti_shuffle(parameter_string: str) -> str:
    words_array: List[str] = parameter_string.split(" ")
    words_sorted_collection: List[str] = []
    index_counter: int = 0

    while index_counter < len(words_array):
        current_word: str = words_array[index_counter]
        char_array: List[str] = []
        char_index: int = 0

        while char_index < len(current_word):
            char_element: str = current_word[char_index]
            char_array.append(char_element)
            char_index += 1

        sorted_characters_temp: List[str] = sorted(char_array)
        reconstructed_word: str = "".join(sorted_characters_temp)
        words_sorted_collection.append(reconstructed_word)
        index_counter += 1

    final_output: str = " ".join(words_sorted_collection)
    return final_output