from typing import List


def anti_shuffle(input_string: str) -> str:
    words_container: List[str] = []
    sorted_collection: List[str] = []
    index_tracker: int = 0

    temp_input_split: List[str] = input_string.split(" ")
    while index_tracker < len(temp_input_split):
        words_container.append(temp_input_split[index_tracker])
        index_tracker += 1

    cursor: int = 0
    while cursor < len(words_container):
        char_list: List[str] = []
        pos: int = 0
        curr_word: str = words_container[cursor]

        while pos < len(curr_word):
            char_list.append(curr_word[pos])
            pos += 1

        char_list.sort()

        reconstructed_word: str = ""
        char_idx: int = 0

        while char_idx < len(char_list):
            reconstructed_word += char_list[char_idx]
            char_idx += 1

        sorted_collection.append(reconstructed_word)
        cursor += 1

    final_output: str = ""
    i: int = 0
    while i < len(sorted_collection):
        final_output += sorted_collection[i]
        if (i + 1) != len(sorted_collection):
            final_output += " "
        i += 1

    return final_output