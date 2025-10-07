from typing import List

def anti_shuffle(s: str) -> str:
    words: List[str] = s.split(' ')
    sorted_words: List[str] = []
    for i in words:
        characters: List[str] = list(i)
        sorted_characters: List[str] = sorted(characters)
        sorted_word: str = ''.join(sorted_characters)
        sorted_words.append(sorted_word)
    result: str = ' '.join(sorted_words)
    return result