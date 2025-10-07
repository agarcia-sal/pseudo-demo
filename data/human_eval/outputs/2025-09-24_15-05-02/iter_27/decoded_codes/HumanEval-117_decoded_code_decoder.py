from typing import List

def select_words(s: str, n: int) -> List[str]:
    if n < 0:
        raise ValueError("n must be non-negative")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result: List[str] = []
    for word in s.split():
        n_consonants: int = sum(1 for ch in word.lower() if ch.isalpha() and ch not in vowels)
        if n_consonants == n:
            result.append(word)
    return result