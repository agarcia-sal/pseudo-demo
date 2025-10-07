from typing import List

def select_words(s: str, n: int) -> List[str]:
    result: List[str] = []
    words = s.split(" ")
    words_count = len(words)
    index_word = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index_word < words_count:
        word = words[index_word]
        n_consonants = 0
        word_length = len(word)
        index_char = 0
        while index_char < word_length:
            char_lower = word[index_char].lower()
            if char_lower not in vowels and char_lower.isalpha():
                n_consonants += 1
            index_char += 1
        if n_consonants == n:
            result.append(word)
        index_word += 1
    return result