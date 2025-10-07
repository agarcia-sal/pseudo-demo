from collections import deque
from typing import Deque, List


def anti_shuffle(input_string: str) -> str:
    words_collection: Deque[str] = deque(input_string.split(' '))
    processed_words: List[str] = []

    while words_collection:
        current_word: str = words_collection.popleft()
        char_array: List[str] = list(current_word)
        char_array.sort()  # ascending sort
        reordered_word: str = ''.join(char_array)
        processed_words.append(reordered_word)

    output_string: str = ' '.join(processed_words)
    return output_string