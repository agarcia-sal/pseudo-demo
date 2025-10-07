from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    collected_words: List[str] = []
    tokens = string_s.split(" ")
    for token in tokens:
        count_consonants = sum(1 for ch in token.lower() if ch.isalpha() and ch not in vowels)
        if count_consonants == natural_number_n:
            collected_words.append(token)
    return collected_words