from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    filtered_words: List[str] = []
    split_words = string_s.split(" ")
    pos = 0
    while pos < len(split_words):
        current_word = split_words[pos]
        consonant_counter = 0
        idx = 0
        while idx < len(current_word):
            ch_lower = current_word[idx].lower()
            if ch_lower in {"a", "e", "i", "o", "u"}:
                pass  # vowel, do nothing
            else:
                consonant_counter += 1
            idx += 1
        if consonant_counter == natural_number_n:
            filtered_words.append(current_word)
        pos += 1
    return filtered_words