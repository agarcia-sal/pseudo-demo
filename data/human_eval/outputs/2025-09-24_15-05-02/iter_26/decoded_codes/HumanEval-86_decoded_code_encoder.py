from typing import List

def anti_shuffle(string_s: str) -> str:
    list_of_words: List[str] = string_s.split(' ')
    list_of_ordered_words: List[str] = []
    for word in list_of_words:
        sorted_characters: List[str] = sorted(word)
        ordered_word: str = ''.join(sorted_characters)
        list_of_ordered_words.append(ordered_word)
    ordered_string: str = ' '.join(list_of_ordered_words)
    return ordered_string