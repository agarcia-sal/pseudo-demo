from typing import List

def anti_shuffle(s: str) -> str:
    words: List[str] = s.split(' ')
    sorted_words: List[str] = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)