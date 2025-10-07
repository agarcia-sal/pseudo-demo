from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected: List[str] = []

    def is_consonant(char_x: str) -> bool:
        return char_x.lower() not in {"a", "e", "i", "o", "u"}

    def count_consonants(word_q: str, idx_r: int, count_t: int) -> int:
        if idx_r >= len(word_q):
            return count_t
        return count_consonants(word_q, idx_r + 1, count_t + (1 if is_consonant(word_q[idx_r]) else 0))

    for lexeme_u in string_s.split(" "):
        if count_consonants(lexeme_u, 0, 0) == natural_number_n:
            collected.append(lexeme_u)

    return collected