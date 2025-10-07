from typing import List

def anti_shuffle(s: str) -> str:
    words: List[str] = s.split(' ')
    ordered_words: List[str] = []
    for i in words:
        chars_list: List[str] = list(i)
        sorted_chars: List[str] = sorted(chars_list)
        ordered_word: str = ''.join(sorted_chars)
        ordered_words.append(ordered_word)
    result: str = ' '.join(ordered_words)
    return result