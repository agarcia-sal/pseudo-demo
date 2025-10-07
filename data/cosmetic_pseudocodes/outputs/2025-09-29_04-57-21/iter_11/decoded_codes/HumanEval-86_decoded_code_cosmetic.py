from typing import List

def anti_shuffle(input_string: str) -> str:
    tokens: List[str] = input_string.split(" ")
    reordered_words: List[str] = []
    index_counter: int = 0

    while index_counter < len(tokens):
        current_word: str = tokens[index_counter]
        characters: List[str] = list(current_word)

        ascending_order_chars: List[str] = []
        char_pos: int = 0

        while char_pos < len(characters):
            ascending_order_chars.append(characters[char_pos])
            char_pos += 1

        ascending_order_chars.sort()  # sorts by ASCII increasing by default

        ordered_word: str = ""
        char_index: int = 0

        while char_index < len(ascending_order_chars):
            ordered_word += ascending_order_chars[char_index]
            char_index += 1

        reordered_words.append(ordered_word)
        index_counter += 1

    final_output: str = ""
    word_index: int = 0

    while word_index < len(reordered_words):
        final_output += reordered_words[word_index]
        if word_index + 1 < len(reordered_words):
            final_output += " "
        word_index += 1

    return final_output