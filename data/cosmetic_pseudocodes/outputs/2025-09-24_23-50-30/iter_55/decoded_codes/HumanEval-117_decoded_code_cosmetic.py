from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    accumulator: List[str] = []

    def count_consonants(word: str, pos: int, acc: int) -> int:
        if pos >= len(word):
            return acc
        ch = word[pos].lower()
        is_cons = ch not in {"a", "e", "i", "o", "u"}
        return count_consonants(word, pos + 1, acc + (1 if is_cons else 0))

    def process_words(words: List[str], idx: int) -> None:
        if idx >= len(words):
            return
        current_word = words[idx]
        cons_count = count_consonants(current_word, 0, 0)
        if cons_count == natural_number_n:
            accumulator.append(current_word)
        process_words(words, idx + 1)

    split_list = string_s.split(" ")
    process_words(split_list, 0)
    return accumulator