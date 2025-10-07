from typing import List


def anti_shuffle(input_string: str) -> str:
    words_collection: List[str] = input_string.split(' ')
    processed_words: List[str] = []

    index_counter: int = 0
    while index_counter < len(words_collection):
        current_word: str = words_collection[index_counter]

        temp_char_array: List[str] = []
        char_index: int = 0
        while char_index < len(current_word):
            temp_char_array.append(current_word[char_index])
            char_index += 1

        sorted_temp_array: List[str] = sorted(temp_char_array)

        word_builder: str = ''
        assemble_index: int = 0
        while assemble_index < len(sorted_temp_array):
            word_builder += sorted_temp_array[assemble_index]
            assemble_index += 1

        processed_words.append(word_builder)
        index_counter += 1

    output_string: str = ''
    output_index: int = 0
    while output_index < len(processed_words):
        if output_index != 0:
            output_string += ' '
        output_string += processed_words[output_index]
        output_index += 1

    return output_string