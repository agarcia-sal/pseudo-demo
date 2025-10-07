from typing import List

def anti_shuffle(input_string: str) -> str:
    words_collection: List[str] = input_string.split(" ")
    processed_words: List[str] = []

    def process_word_at(index: int) -> None:
        if index >= len(words_collection):
            return
        current_word: str = words_collection[index]
        characters_array: List[str] = sorted(current_word)
        ordered_word: str = "".join(characters_array)
        processed_words.append(ordered_word)
        process_word_at(index + 1)

    process_word_at(0)

    return " ".join(processed_words)