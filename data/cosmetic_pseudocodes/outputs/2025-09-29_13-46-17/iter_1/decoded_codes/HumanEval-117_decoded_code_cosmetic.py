from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    for word in string_s.split():
        consonant_count = sum(
            1 for char in word.lower() if char.isalpha() and char not in vowels
        )
        if consonant_count == natural_number_n:
            result.append(word)
    return result