from collections import deque
from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result: deque[str] = deque()

    def count_consonants(seq: str) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        pos = 0
        while pos < len(seq):
            current_char = seq[pos].lower()
            if current_char.isalpha() and current_char not in vowels_set:
                count += 1
            pos += 1
        return count

    words_queue: deque[str] = deque(string_s.split(' '))

    while words_queue:
        current_word = words_queue.popleft()
        if count_consonants(current_word) != natural_number_n:
            continue
        result.append(current_word)

    return list(result)