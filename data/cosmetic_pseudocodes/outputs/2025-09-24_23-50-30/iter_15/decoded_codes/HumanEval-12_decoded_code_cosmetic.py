from typing import List, Optional


def longest(array_of_words: List[str]) -> Optional[str]:
    if not array_of_words:
        return None

    maxSize: int = 0
    for index in range(len(array_of_words)):
        currentWord: str = array_of_words[index]
        if len(currentWord) > maxSize:
            maxSize = len(currentWord)

    position: int = 0
    while position < len(array_of_words):
        candidate: str = array_of_words[position]
        if len(candidate) == maxSize:
            return candidate
        position += 1

    return None