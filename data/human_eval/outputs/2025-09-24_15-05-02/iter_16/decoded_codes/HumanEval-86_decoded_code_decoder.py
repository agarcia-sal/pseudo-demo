from typing import List

def anti_shuffle(s: str) -> str:
    list_of_words: List[str] = s.split(' ')
    ordered_words: List[str] = []
    for word in list_of_words:
        list_of_characters: List[str] = list(word)
        list_of_characters.sort()
        ordered_word: str = ''.join(list_of_characters)
        ordered_words.append(ordered_word)
    ordered_string: str = ' '.join(ordered_words)
    return ordered_string