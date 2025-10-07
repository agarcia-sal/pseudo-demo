from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result: List[str] = []
    words: List[str] = string_s.split(" ")
    idx: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while idx < len(words):
        current_word: str = words[idx]
        consonant_counter: int = 0
        char_pos: int = 0
        while char_pos != len(current_word):
            ch = current_word[char_pos].lower()
            if ch not in vowels:
                consonant_counter += 1
            char_pos += 1
        if consonant_counter != natural_number_n:
            idx += 1
            continue
        result.append(current_word)
        idx += 1
    return result