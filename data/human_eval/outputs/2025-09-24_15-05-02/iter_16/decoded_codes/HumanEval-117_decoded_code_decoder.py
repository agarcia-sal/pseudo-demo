from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    for word in string_s.split():
        n_consonants = 0
        for index in range(len(word)):
            char = word[index].lower()
            if char not in vowels:
                n_consonants += 1
        if n_consonants == natural_number_n:
            result.append(word)
    return result