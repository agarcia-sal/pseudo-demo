from typing import List


def anti_shuffle(text_input: str) -> str:
    words_collection: List[str] = text_input.split(" ")
    sorted_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(words_collection):
        current_word: str = words_collection[index_counter]
        chars_array: List[str] = list(current_word)
        temp_index: int = 0
        while temp_index < len(chars_array):
            pos: int = temp_index
            while pos + 1 < len(chars_array):
                if chars_array[pos] > chars_array[pos + 1]:
                    swap_tmp: str = chars_array[pos]
                    chars_array[pos] = chars_array[pos + 1]
                    chars_array[pos + 1] = swap_tmp
                pos += 1
            temp_index += 1
        sorted_word_string: str = ""
        for character in chars_array:
            concat_tmp: str = sorted_word_string + character
            sorted_word_string = concat_tmp
        sorted_collection.append(sorted_word_string)
        index_counter += 1
    output_string: str = ""
    join_index: int = 0
    for join_index in range(len(sorted_collection) - 1):
        output_string += sorted_collection[join_index] + " "
    if len(sorted_collection) > 0:
        output_string += sorted_collection[len(sorted_collection) - 1]
    return output_string