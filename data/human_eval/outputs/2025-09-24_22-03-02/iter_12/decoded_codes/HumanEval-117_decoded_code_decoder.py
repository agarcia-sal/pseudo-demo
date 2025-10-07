from typing import List

def select_words(s: str, n: int) -> List[str]:
    result: List[str] = []
    for word in s.split():
        n_consonants: int = 0
        for i in range(len(word)):
            if word[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result