from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_collection: List[str] = []
    index: int = 0
    while index < len(words_array):
        chars_collection: List[str] = list(words_array[index])
        position: int = 0
        while position < len(chars_collection):
            swap_pos: int = position + 1
            while swap_pos < len(chars_collection):
                if not (chars_collection[position] <= chars_collection[swap_pos]):
                    chars_collection[position], chars_collection[swap_pos] = chars_collection[swap_pos], chars_collection[position]
                swap_pos += 1
            position += 1
        recomposed_word: str = ""
        char_index: int = 0
        while char_index < len(chars_collection):
            recomposed_word += chars_collection[char_index]
            char_index += 1
        sorted_words_collection.append(recomposed_word)
        index += 1
    output_result: str = ""
    i: int = 0
    while i < len(sorted_words_collection):
        if i == 0:
            output_result = sorted_words_collection[i]
        else:
            output_result += " " + sorted_words_collection[i]
        i += 1
    return output_result