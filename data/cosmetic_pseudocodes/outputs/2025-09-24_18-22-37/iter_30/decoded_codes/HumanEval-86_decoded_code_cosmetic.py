from typing import List


def anti_shuffle(original_text: str) -> str:
    words_collection: List[str] = original_text.split(" ")
    normalized_words: List[str] = []

    index: int = 0
    while index < len(words_collection):
        current_word: str = words_collection[index]
        characters_array: List[str] = []

        char_index: int = 0
        while char_index < len(current_word):
            characters_array.append(current_word[char_index])
            char_index += 1

        ordered_characters: List[str] = sorted(characters_array)
        temp_word: str = "".join(ordered_characters)
        normalized_words.append(temp_word)

        index += 1

    final_output: str = " ".join(normalized_words)
    return final_output