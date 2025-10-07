from typing import List


def anti_shuffle(string_input: str) -> str:
    list_of_words: List[str] = string_input.split(' ')
    list_of_sorted_words: List[str] = []
    for word in list_of_words:
        list_of_characters: List[str] = list(word)
        sorted_characters: List[str] = sorted(list_of_characters)
        sorted_word: str = ''.join(sorted_characters)
        list_of_sorted_words.append(sorted_word)
    ordered_string: str = ' '.join(list_of_sorted_words)
    return ordered_string