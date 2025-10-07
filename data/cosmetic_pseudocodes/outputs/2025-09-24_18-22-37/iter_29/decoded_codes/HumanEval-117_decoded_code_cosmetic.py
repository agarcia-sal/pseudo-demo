from typing import List


def select_words(string_c: str, p: int) -> List[str]:
    output_sequence: List[str] = []
    words_collection = string_c.split(" ")
    pos_i = 0
    vowels = {"a", "e", "i", "o", "u"}
    while pos_i < len(words_collection):
        current_word = words_collection[pos_i]
        consonant_count = 0
        idx_j = 0
        while idx_j < len(current_word):
            chr_x = current_word[idx_j].lower()
            if chr_x not in vowels:
                consonant_count += 1
            idx_j += 1
        if consonant_count == p:
            output_sequence.append(current_word)
        pos_i += 1
    return output_sequence