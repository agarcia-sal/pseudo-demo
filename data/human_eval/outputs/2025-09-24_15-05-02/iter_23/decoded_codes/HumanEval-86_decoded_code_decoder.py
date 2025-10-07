from typing import List

def anti_shuffle(input_string: str) -> str:
    list_of_words: List[str] = input_string.split(' ')
    ordered_words: List[str] = []
    for word in list_of_words:
        list_of_characters: List[str] = list(word)
        list_of_characters.sort()
        sorted_word: str = ''.join(list_of_characters)
        ordered_words.append(sorted_word)
    ordered_string: str = ' '.join(ordered_words)
    return ordered_string