from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected: List[str] = []
    words_list = string_s.split(" ")

    word_iter = 0
    while word_iter < len(words_list):
        current_word = words_list[word_iter]
        consonant_tally = 0

        char_iter = 0
        while char_iter < len(current_word):
            lower_char = current_word[char_iter].lower()
            if lower_char not in ("a", "e", "i", "o", "u"):
                consonant_tally += 1
            char_iter += 1

        if consonant_tally == natural_number_n:
            collected.append(current_word)

        word_iter += 1

    return collected