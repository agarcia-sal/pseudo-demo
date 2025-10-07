from typing import List

def anti_shuffle(input_string: str) -> str:
    list_of_words: List[str] = input_string.split(' ')
    ordered_words: List[str] = []
    for word in list_of_words:
        sorted_chars = sorted(word)
        new_word = ''.join(sorted_chars)
        ordered_words.append(new_word)
    ordered_string = ' '.join(ordered_words)
    return ordered_string