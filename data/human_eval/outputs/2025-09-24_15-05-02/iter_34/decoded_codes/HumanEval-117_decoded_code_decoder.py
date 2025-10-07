from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    for word in string_s.split():
        number_of_consonants = sum(
            1 for ch in word if ch.lower() not in vowels
        )
        if number_of_consonants == natural_number_n:
            result.append(word)
    return result