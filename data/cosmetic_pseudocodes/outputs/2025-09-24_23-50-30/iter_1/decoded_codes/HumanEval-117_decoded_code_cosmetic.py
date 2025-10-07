from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = string_s.split(' ')
    result: List[str] = []
    for current_word in words:
        consonant_count = sum(
            1 for ch in current_word.lower() if ch.isalpha() and ch not in vowels
        )
        if consonant_count == natural_number_n:
            result.append(current_word)
    return result