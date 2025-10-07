from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    list_words_selected: List[str] = []
    list_words = string_s.split(" ")
    index_words = 0

    vowels = {'a', 'e', 'i', 'o', 'u'}

    while index_words < len(list_words):
        current_word = list_words[index_words]
        index_words += 1

        count_consonants = 0
        idx_char = 0
        while idx_char < len(current_word):
            char_lower = current_word[idx_char].lower()
            is_vowel = char_lower in vowels
            if not is_vowel:
                count_consonants += 1
            idx_char += 1

        if count_consonants == natural_number_n:
            list_words_selected.append(current_word)

    return list_words_selected