from typing import List

def anti_shuffle(original_text: str) -> str:
    words_collection: List[str] = original_text.split(" ")
    reordered_words: List[str] = []
    idx: int = 0
    while idx < len(words_collection):
        current_word: str = words_collection[idx]
        chars_array: List[str] = list(current_word)
        sorted_chars: List[str] = []
        while len(chars_array) > 0:
            min_char: str = chr(127)
            min_index: int = -1
            pos: int = 0
            while pos < len(chars_array):
                if chars_array[pos] < min_char:
                    min_char = chars_array[pos]
                    min_index = pos
                pos += 1
            if min_index != -1:
                sorted_chars.append(min_char)
                chars_array.pop(min_index)
        assembled_word: str = ""
        letter_pos: int = 0
        while letter_pos < len(sorted_chars):
            assembled_word += sorted_chars[letter_pos]
            letter_pos += 1
        reordered_words.append(assembled_word)
        idx += 1
    final_output: str = ""
    concat_index: int = 0
    while concat_index < len(reordered_words):
        final_output += reordered_words[concat_index]
        if concat_index != len(reordered_words) - 1:
            final_output += " "
        concat_index += 1
    return final_output