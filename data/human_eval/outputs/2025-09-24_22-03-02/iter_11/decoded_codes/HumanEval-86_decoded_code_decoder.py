from typing import List

def anti_shuffle(s: str) -> str:
    words: List[str] = s.split()
    sorted_words: List[str] = []
    for i in words:
        chars = sorted(i)
        sorted_word = ''.join(chars)
        sorted_words.append(sorted_word)
    return ' '.join(sorted_words)