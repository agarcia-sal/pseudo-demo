from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_collection: List[str] = []
    for index in range(len(words_array)):
        characters_list: List[str] = list(words_array[index])
        characters_list.sort()
        assembled_word = "".join(characters_list)
        sorted_words_collection.append(assembled_word)
    final_output: str = " ".join(sorted_words_collection)
    return final_output