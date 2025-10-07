from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(words_array):
        current_word: str = words_array[index_counter]
        character_list: List[str] = list(current_word)
        character_list.sort()
        reconstructed_word: str = "".join(character_list)
        sorted_words_collection.append(reconstructed_word)
        index_counter += 1
    joined_result: str = ""
    for i in range(len(sorted_words_collection)):
        joined_result += sorted_words_collection[i]
        if i < len(sorted_words_collection) - 1:
            joined_result += " "
    return joined_result