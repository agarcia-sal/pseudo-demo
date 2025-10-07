from typing import List

def select_words(string_s: str, number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    for word in string_s.split():
        n_consonants = sum(1 for ch in word if ch.lower() not in vowels)
        if n_consonants == number_n:
            result.append(word)
    return result