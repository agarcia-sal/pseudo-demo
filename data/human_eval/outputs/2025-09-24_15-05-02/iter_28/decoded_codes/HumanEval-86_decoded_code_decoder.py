from typing import List

def anti_shuffle(s: str) -> str:
    list_of_words: List[str] = s.split(' ')
    ordered_words: List[str] = []
    for word in list_of_words:
        sorted_word: str = ''.join(sorted(word))
        ordered_words.append(sorted_word)
    result_string: str = ' '.join(ordered_words)
    return result_string