from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    filtered_words: List[str] = []
    word_list = string_s.split(" ")
    for position in range(len(word_list)):
        current_word = word_list[position]
        consonant_tally = sum(
            1 for char in current_word if char.lower() not in vowels
        )
        if consonant_tally == natural_number_n:
            filtered_words.append(current_word)
    return filtered_words