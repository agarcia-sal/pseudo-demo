from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collection: List[str] = []
    words_list: List[str] = string_s.split(" ")
    position: int = 0
    vowels = {"a", "e", "i", "o", "u"}

    while position < len(words_list):
        current_word = words_list[position]
        consonant_count = 0
        idx = 0
        while idx < len(current_word):
            current_char = current_word[idx].lower()
            if current_char not in vowels and current_char.isalpha():
                consonant_count += 1
            idx += 1
        if consonant_count == natural_number_n:
            collection.append(current_word)
        position += 1

    return collection