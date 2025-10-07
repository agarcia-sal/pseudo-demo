from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    processed_words: List[str] = []
    index: int = 0
    while index < len(words_array):
        current_word: str = words_array[index]
        char_list: List[str] = list(current_word)
        i: int = 1
        while i < len(char_list):
            j: int = i
            while j > 0 and char_list[j - 1] > char_list[j]:
                char_list[j - 1], char_list[j] = char_list[j], char_list[j - 1]
                j -= 1
            i += 1
        reconstructed_word: str = ""
        k: int = 0
        while k < len(char_list):
            reconstructed_word += char_list[k]
            k += 1
        processed_words.append(reconstructed_word)
        index += 1
    final_result: str = ""
    pos: int = 0
    while pos < len(processed_words):
        if pos > 0:
            final_result += " "
        final_result += processed_words[pos]
        pos += 1
    return final_result