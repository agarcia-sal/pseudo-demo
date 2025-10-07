from typing import List

def select_words(s: str, n: int) -> List[str]:
    result: List[str] = []
    if s == "":
        return result

    words: List[str] = []
    temp_word: str = ""
    length_s: int = len(s)
    index_s: int = 0
    while index_s < length_s:
        char: str = s[index_s]
        if char == " ":
            if temp_word != "":
                words.append(temp_word)
                temp_word = ""
        else:
            temp_word += char
        index_s += 1
    if temp_word != "":
        words.append(temp_word)

    index_word: int = 0
    length_words: int = len(words)
    while index_word < length_words:
        word: str = words[index_word]
        n_consonants: int = 0
        index_char: int = 0
        length_word: int = len(word)
        while index_char < length_word:
            current_char: str = word[index_char]
            lower_char: str = current_char.lower()
            if lower_char not in ("a", "e", "i", "o", "u"):
                n_consonants += 1
            index_char += 1
        if n_consonants == n:
            result.append(word)
        index_word += 1

    return result