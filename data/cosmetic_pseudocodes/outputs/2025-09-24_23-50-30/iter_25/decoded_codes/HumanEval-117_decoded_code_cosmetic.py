from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    collected_words: List[str] = []
    word_list = string_s.split(' ')
    for text_token in word_list:
        consonant_counter = 0
        position = 0
        while position < len(text_token):
            letter = text_token[position].lower()
            if letter not in vowels:
                consonant_counter += 1
            position += 1
        if consonant_counter == natural_number_n:
            collected_words.append(text_token)
    return collected_words