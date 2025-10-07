from typing import List


def select_words(string_s: str, n: int) -> List[str]:
    output_list: List[str] = []
    splitted_words = string_s.split(" ")
    word_idx = 0
    while word_idx < len(splitted_words):
        current_word = splitted_words[word_idx]

        consonant_sum = 0
        char_pos = 0
        while char_pos < len(current_word):
            current_char = current_word[char_pos].lower()
            if current_char not in {"a", "e", "i", "o", "u"}:
                consonant_sum += 1
            char_pos += 1

        if consonant_sum == n:
            output_list.append(current_word)
        word_idx += 1

    return output_list