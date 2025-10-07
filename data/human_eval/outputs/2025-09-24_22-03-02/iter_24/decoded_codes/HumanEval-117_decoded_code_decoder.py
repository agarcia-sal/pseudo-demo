from typing import List

def select_words(s: str, n: int) -> List[str]:
    result = [""]
    words = []
    current_word = ""
    index = 0
    while index < len(s):
        char = s[index]
        if char == " ":
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
        index += 1
    if len(current_word) > 0:
        words.append(current_word)
    word_index = 0
    while word_index < len(words):
        word = words[word_index]
        n_consonants = 0
        char_index = 0
        while char_index < len(word):
            letter = word[char_index]
            letter_lower = letter.lower()
            if letter_lower not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
            char_index += 1
        if n_consonants == n:
            result.append(word)
        word_index += 1
    return result