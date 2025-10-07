from typing import List

def anti_shuffle(input_string: str) -> str:
    list_of_words: List[str] = input_string.split(' ')
    ordered_words: List[str] = []
    for word in list_of_words:
        characters: List[str] = list(word)
        characters.sort()
        ordered_word: str = ''.join(characters)
        ordered_words.append(ordered_word)
    result_string: str = ' '.join(ordered_words)
    return result_string