from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_results: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for token_word in string_s.split(" "):
        consonant_count = 0
        position = 0
        while position < len(token_word):
            current_char = token_word[position].lower()
            if current_char not in vowels:
                consonant_count += 1
            position += 1
        if consonant_count == natural_number_n:
            collected_results.append(token_word)
    return collected_results