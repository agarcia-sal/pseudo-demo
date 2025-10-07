from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []

    def count_consonants(text: str) -> int:
        tally = 0
        idx = 0
        vowels = {"a", "e", "i", "o", "u"}
        while idx < len(text):
            ch = text[idx].lower()
            if ch.isalpha() and ch not in vowels:
                tally += 1
            idx += 1
        return tally

    for term in string_s.split(" "):
        if count_consonants(term) != natural_number_n:
            continue
        collected_words.append(term)

    return collected_words