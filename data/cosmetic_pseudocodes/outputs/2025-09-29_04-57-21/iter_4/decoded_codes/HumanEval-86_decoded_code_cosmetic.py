from typing import List


def anti_shuffle(input_string: str) -> str:
    word_tokens: List[str] = []
    processed_words: List[str] = []
    idx: int = 0

    word_tokens = input_string.split(" ")

    while idx < len(word_tokens):
        current_token: str = word_tokens[idx]
        character_array: List[str] = []
        char_idx: int = 0

        character_array = []
        for char_idx in range(len(current_token)):
            character_array.append(current_token[char_idx])

        character_array.sort()

        reconstructed_word: str = ""
        build_idx: int = 0

        reconstructed_word = ""
        while build_idx < len(character_array):
            reconstructed_word += character_array[build_idx]
            build_idx += 1

        processed_words.append(reconstructed_word)
        idx += 1

    final_result: str = ""
    word_index: int = 0

    if not processed_words:
        final_result = ""
    else:
        final_result = processed_words[0]
        word_index = 1
        while word_index < len(processed_words):
            final_result += " " + processed_words[word_index]
            word_index += 1

    return final_result