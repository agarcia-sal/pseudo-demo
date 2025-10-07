from typing import List


def select_words(s: str, n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    for word in s.split():
        n_consonants = 0
        for index in range(len(word)):
            if word[index].lower() not in vowels:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result