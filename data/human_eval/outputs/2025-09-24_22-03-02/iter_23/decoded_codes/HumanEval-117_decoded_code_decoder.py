from typing import List

def select_words(s: str, n: int) -> List[str]:
    result: List[str] = []
    words: List[str] = []
    current_word = ""
    s_length = len(s)
    index = 0
    while index < s_length:
        current_char = s[index]
        if current_char == ' ':
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += current_char
        index += 1
    if current_word != "":
        words.append(current_word)
    word_index = 0
    words_count = len(words)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while word_index < words_count:
        word = words[word_index]
        n_consonants = 0
        char_index = 0
        word_length = len(word)
        while char_index < word_length:
            char_lower = word[char_index].lower()
            if char_lower not in vowels:
                n_consonants += 1
            char_index += 1
        if n_consonants == n:
            result.append(word)
        word_index += 1
    return result