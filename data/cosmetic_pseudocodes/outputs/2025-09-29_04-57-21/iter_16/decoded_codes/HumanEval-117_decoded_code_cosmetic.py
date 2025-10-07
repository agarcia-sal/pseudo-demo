from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word_iter = iter(string_s.split())

    for current_word in word_iter:
        consonant_counter = 0
        for current_char in current_word.lower():
            if current_char not in vowels:
                consonant_counter += 1
        if consonant_counter == natural_number_n:
            collected_words.append(current_word)

    return collected_words