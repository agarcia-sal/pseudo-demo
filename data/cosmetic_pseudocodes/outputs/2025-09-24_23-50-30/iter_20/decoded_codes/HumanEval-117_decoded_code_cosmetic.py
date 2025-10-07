from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels_set = {'a', 'e', 'i', 'o', 'u'}

    def count_consonants(string_t: str, current_pos: int, acc: int) -> int:
        if current_pos >= len(string_t):
            return acc
        char_lc = string_t[current_pos].lower()
        is_consonant = char_lc.isalpha() and char_lc not in vowels_set
        return count_consonants(string_t, current_pos + 1, acc + (1 if is_consonant else 0))

    filtered_words: List[str] = []
    splitted_words = string_s.split(' ')

    index = 0
    while index < len(splitted_words):
        current_word = splitted_words[index]
        consonant_count = count_consonants(current_word, 0, 0)
        if consonant_count == natural_number_n:
            filtered_words.append(current_word)
        index += 1

    return filtered_words