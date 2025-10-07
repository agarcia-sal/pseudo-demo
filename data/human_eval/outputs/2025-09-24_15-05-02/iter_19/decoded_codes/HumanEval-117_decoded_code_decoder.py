from typing import List

def select_words(s: str, n: int) -> List[str]:
    result: List[str] = []
    vowels = {"a", "e", "i", "o", "u"}
    for word in s.split():
        n_consonants = 0
        for ch in word:
            if ch.lower() not in vowels:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result