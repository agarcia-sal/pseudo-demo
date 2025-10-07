from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    filtered_words: List[str] = []
    for w in string_s.split(" "):
        consonant_count = sum(1 for ch in w if ch.lower() not in vowels)
        if consonant_count == natural_number_n:
            filtered_words.append(w)
    return filtered_words