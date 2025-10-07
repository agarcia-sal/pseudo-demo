from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    processed_words: List[str] = []
    index: int = 0
    while index < len(words_array):
        word: str = words_array[index]
        characters: List[str] = list(word)
        characters.sort()
        new_word: str = "".join(characters)
        processed_words.append(new_word)
        index += 1
    return " ".join(processed_words)