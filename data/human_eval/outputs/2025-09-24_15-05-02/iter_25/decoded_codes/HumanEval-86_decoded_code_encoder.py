from typing import List

def anti_shuffle(input_string: str) -> str:
    words: List[str] = input_string.split(' ')
    ordered_words: List[str] = []
    for word in words:
        characters: List[str] = list(word)
        sorted_characters: List[str] = sorted(characters)
        ordered_word: str = ''.join(sorted_characters)
        ordered_words.append(ordered_word)
    result: str = ' '.join(ordered_words)
    return result