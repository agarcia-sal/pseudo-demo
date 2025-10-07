from typing import List

def select_words(s: str, n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in s.split():
        n_consonants = 0
        for char in word:
            if char.lower() not in vowels:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result