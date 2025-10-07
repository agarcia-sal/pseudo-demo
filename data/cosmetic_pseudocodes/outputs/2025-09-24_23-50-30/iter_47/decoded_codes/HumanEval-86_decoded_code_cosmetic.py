from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = []
    index_counter: int = 0
    length: int = len(input_string)
    while index_counter < length:
        current_start: int = index_counter
        while index_counter < length and input_string[index_counter] != ' ':
            index_counter += 1
        words_array.append(input_string[current_start:index_counter])
        index_counter += 1  # skip the space

    rearranged_words: List[str] = []
    position_marker: int = 0
    while position_marker < len(words_array):
        char_list: List[str] = []
        char_index: int = 0
        current_word: str = words_array[position_marker]
        while char_index < len(current_word):
            char_list.append(current_word[char_index])
            char_index += 1

        char_count: int = len(char_list)
        swap_idx: int = 0
        # Sorting chars by selection sort as per pseudocode
        while swap_idx < char_count - 1:
            check_idx: int = swap_idx + 1
            while check_idx < char_count:
                if char_list[swap_idx] > char_list[check_idx]:
                    char_list[swap_idx], char_list[check_idx] = char_list[check_idx], char_list[swap_idx]
                check_idx += 1
            swap_idx += 1

        reconstructed_word: str = ""
        build_index: int = 0
        while build_index < char_count:
            reconstructed_word += char_list[build_index]
            build_index += 1

        rearranged_words.append(reconstructed_word)
        position_marker += 1

    output_string: str = ""
    output_pos: int = 0
    while output_pos < len(rearranged_words):
        output_string += rearranged_words[output_pos]
        if output_pos < len(rearranged_words) - 1:
            output_string += " "
        output_pos += 1

    return output_string