from typing import List


def anti_shuffle(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    words: List[str] = s.split(' ')
    ordered_words: List[str] = [''.join(sorted(word)) for word in words]
    result_string: str = ' '.join(ordered_words)
    return result_string