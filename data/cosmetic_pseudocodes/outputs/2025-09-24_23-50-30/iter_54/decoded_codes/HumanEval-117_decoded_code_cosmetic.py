from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    selected_words: List[str] = []

    def count_nonvowels(seq: str, pos: int, acc: int) -> int:
        if pos >= len(seq):
            return acc
        if seq[pos].lower() not in {"a", "e", "i", "o", "u"}:
            return count_nonvowels(seq, pos + 1, acc + 1)
        return count_nonvowels(seq, pos + 1, acc)

    for current_word in string_s.split(" "):
        consonant_counter = count_nonvowels(current_word, 0, 0)
        if consonant_counter == natural_number_n:
            selected_words.append(current_word)

    return selected_words