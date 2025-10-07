from collections import deque
from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_results: List[str] = []
    words_queue: deque[str] = deque(string_s.split(" "))

    def count_consonants(word_str: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonant_count = 0
        for ch in word_str.lower():
            if ch.isalpha() and ch not in vowels:
                consonant_count += 1
        return consonant_count

    def process_words(queue_ref: deque[str]) -> None:
        if not queue_ref:
            return
        current_word = queue_ref.popleft()
        consonants = count_consonants(current_word)
        if consonants == natural_number_n:
            collected_results.append(current_word)
        process_words(queue_ref)

    process_words(words_queue)
    return collected_results