from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    words = string_s.split(" ")
    for word in words:
        consonant_count = sum(1 for ch in word if ch.lower() not in vowels)
        if consonant_count == natural_number_n:
            result.append(word)
    return result