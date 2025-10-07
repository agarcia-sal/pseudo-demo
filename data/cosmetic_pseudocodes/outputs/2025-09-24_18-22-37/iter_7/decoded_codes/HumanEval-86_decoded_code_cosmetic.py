from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_collection: List[str] = []
    idx: int = 0
    while idx < len(words_array):
        current_word: str = words_array[idx]
        characters_list: List[str] = list(current_word)
        temp_idx: int = 0
        while temp_idx < len(characters_list) - 1:
            next_idx: int = temp_idx + 1
            while next_idx < len(characters_list):
                if characters_list[temp_idx] > characters_list[next_idx]:
                    characters_list[temp_idx], characters_list[next_idx] = characters_list[next_idx], characters_list[temp_idx]
                next_idx += 1
            temp_idx += 1
        sorted_word_string: str = ""
        char_idx: int = 0
        while char_idx < len(characters_list):
            sorted_word_string += characters_list[char_idx]
            char_idx += 1
        sorted_words_collection.append(sorted_word_string)
        idx += 1
    output_string: str = ""
    join_index: int = 0
    while join_index < len(sorted_words_collection):
        output_string += sorted_words_collection[join_index]
        if join_index + 1 < len(sorted_words_collection):
            output_string += " "
        join_index += 1
    return output_string