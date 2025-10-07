from typing import List


def anti_shuffle(input_string: str) -> str:
    temp_words: List[str] = input_string.split(" ")
    accumulated_sorted_words: List[str] = []
    idx_counter: int = 0
    while True:
        if idx_counter >= len(temp_words):
            break
        current_word: str = temp_words[idx_counter]
        char_list: List[str] = []
        char_index: int = 0
        while char_index < len(current_word):
            char_list.append(current_word[char_index])
            char_index += 1
        char_list_sorted: List[str] = []
        remaining_chars: List[str] = char_list[:]
        while len(remaining_chars) > 0:
            min_char: str = remaining_chars[0]
            for element in remaining_chars:
                if element < min_char:
                    min_char = element
            char_list_sorted.append(min_char)
            remaining_chars.remove(min_char)
        reformed_word: str = ""
        for character_element in char_list_sorted:
            reformed_word += character_element
        accumulated_sorted_words.append(reformed_word)
        idx_counter += 1
    output_string: str = ""
    combined_index: int = 0
    while combined_index < len(accumulated_sorted_words):
        output_string += accumulated_sorted_words[combined_index]
        if combined_index != (len(accumulated_sorted_words) - 1):
            output_string += " "
        combined_index += 1
    return output_string