from typing import List, Tuple


def find_max(list_of_words: List[str]) -> str:
    def longest_unique_chars(word: str) -> int:
        unique_chars = set()
        pos = 0
        while True:
            if pos >= len(word):
                break
            unique_chars.add(word[pos])
            pos += 1
        return len(unique_chars)

    indexed: List[Tuple[str, int]] = []
    i = 0
    while i < len(list_of_words):
        indexed.append((list_of_words[i], -longest_unique_chars(list_of_words[i])))
        i += 1

    def swap(a: int, b: int) -> None:
        indexed[a], indexed[b] = indexed[b], indexed[a]

    j = 0
    n = len(indexed)
    while j < n - 1:
        k = 0
        while k < n - j - 1:
            curr_word, curr_score = indexed[k]
            next_word, next_score = indexed[k + 1]
            if not (
                (curr_score < next_score)
                or (curr_score == next_score and curr_word <= next_word)
            ):
                swap(k, k + 1)
            k += 1
        j += 1

    return indexed[0][0]