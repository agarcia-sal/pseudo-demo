from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(single_word: str) -> int:
        count = 0
        for ch in single_word.lower():
            if ch.isalpha() and ch not in {'a', 'e', 'i', 'o', 'u'}:
                count += 1
        return count

    words_array = string_s.split(" ")
    collected_words: List[str] = [term for term in words_array if count_consonants(term) == natural_number_n]

    return collected_words