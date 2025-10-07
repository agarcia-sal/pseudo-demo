from typing import List

def select_words(s: str, n: int) -> List[str]:
    result: List[str] = [""]
    words: List[str] = [""]
    current_word: str = ""
    for character_index in range(len(s)):
        if s[character_index] == " ":
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ""
        else:
            current_word += s[character_index]
    if len(current_word) > 0:
        words.append(current_word)
    for word_index in range(len(words)):
        word = words[word_index]
        n_consonants = 0
        for i in range(len(word)):
            char_lower = word[i].lower()
            if char_lower not in {"a", "e", "i", "o", "u"}:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result