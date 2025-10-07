from typing import List

def select_words(s: str, n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for word in s.split():
        n_consonants = sum(ch.lower() not in vowels for ch in word)
        if n_consonants == n:
            result.append(word)
    return result