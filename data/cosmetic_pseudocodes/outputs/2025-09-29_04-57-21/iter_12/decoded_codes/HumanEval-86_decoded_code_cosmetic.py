from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words: List[str] = []
    index: int = 0
    while index < len(words_array):
        current_word: str = words_array[index]
        char_sequence: List[str] = list(current_word)
        sorted_sequence: List[str] = sorted(char_sequence)
        reconstructed_word: str = "".join(sorted_sequence)
        sorted_words.append(reconstructed_word)
        index += 1
    combined_result: str = " ".join(sorted_words)
    return combined_result