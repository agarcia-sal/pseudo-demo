from typing import List

def anti_shuffle(s: str) -> str:
    words: List[str] = s.split(' ')
    sorted_words: List[str] = []
    for word in words:
        sorted_word: str = ''.join(sorted(word))
        sorted_words.append(sorted_word)
    result: str = ' '.join(sorted_words)
    return result