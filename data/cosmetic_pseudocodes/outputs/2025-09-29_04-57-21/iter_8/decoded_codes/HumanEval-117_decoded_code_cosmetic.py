from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    word_list: List[str] = []
    pos: int = 0
    length = len(string_s)

    while pos < length:
        start = pos
        while pos < length and string_s[pos] != ' ':
            pos += 1
        word_list.append(string_s[start:pos])
        pos += 1  # move past the space

    for current_word in word_list:
        cnt_non_vowels = 0
        for letter in current_word.lower():
            if letter not in {'a', 'e', 'i', 'o', 'u'}:
                cnt_non_vowels += 1
        if cnt_non_vowels == natural_number_n:
            collected_words.append(current_word)

    return collected_words