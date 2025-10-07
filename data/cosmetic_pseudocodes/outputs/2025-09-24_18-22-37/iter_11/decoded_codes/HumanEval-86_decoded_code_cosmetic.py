from typing import List


def anti_shuffle(input_string: str) -> str:
    words_collection: List[str] = input_string.split(" ")
    sorted_words_collection: List[str] = []
    index_counter: int = 0

    while index_counter < len(words_collection):
        current_word: str = words_collection[index_counter]
        chars_array: List[str] = []
        char_index: int = 0

        while char_index < len(current_word):
            chars_array.append(current_word[char_index])
            char_index += 1

        sorted_chars_array: List[str] = sorted(chars_array)
        assembled_sorted_word: str = ""
        assemble_index: int = 0

        while assemble_index < len(sorted_chars_array):
            assembled_sorted_word += sorted_chars_array[assemble_index]
            assemble_index += 1

        sorted_words_collection.append(assembled_sorted_word)
        index_counter += 1

    result_var: str = ""
    sorted_index: int = 0

    while sorted_index < len(sorted_words_collection):
        if sorted_index == 0:
            result_var = sorted_words_collection[sorted_index]
        else:
            result_var += " " + sorted_words_collection[sorted_index]
        sorted_index += 1

    return result_var