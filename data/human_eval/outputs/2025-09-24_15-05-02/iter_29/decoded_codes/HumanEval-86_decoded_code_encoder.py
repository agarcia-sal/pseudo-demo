from typing import List


def anti_shuffle(input_string: str) -> str:
    list_of_words: List[str] = input_string.split(' ')
    list_of_ordered_words: List[str] = []
    for word in list_of_words:
        sorted_characters: List[str] = sorted(word)
        ordered_word: str = ''.join(sorted_characters)
        list_of_ordered_words.append(ordered_word)
    result_string: str = ' '.join(list_of_ordered_words)
    return result_string