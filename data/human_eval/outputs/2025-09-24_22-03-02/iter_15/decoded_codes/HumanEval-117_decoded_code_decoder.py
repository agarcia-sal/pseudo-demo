from typing import List

def select_words(s: str, n: int) -> List[str]:
    result = [""]
    list_of_words = s.split()
    for word in list_of_words:
        n_consonants = 0
        length_of_word = len(word)
        for i in range(length_of_word):
            character_lowercase = word[i].lower()
            if character_lowercase not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result