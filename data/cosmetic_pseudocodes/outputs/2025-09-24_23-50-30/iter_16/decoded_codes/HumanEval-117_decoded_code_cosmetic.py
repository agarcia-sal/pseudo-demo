from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(sequence_p: str, position_q: int) -> int:
        if position_q >= len(sequence_p):
            return 0
        current_letter = sequence_p[position_q].lower()
        is_consonant = current_letter not in {"a", "e", "i", "o", "u"}
        return (1 if is_consonant else 0) + count_consonants(sequence_p, position_q + 1)

    separated_words: List[str] = []
    for char in string_s:
        if char == " ":
            separated_words.append("")
        else:
            if not separated_words:
                separated_words.append(char)
            else:
                separated_words[-1] += char

    filtered_words: List[str] = []
    iterator_k = 0
    while iterator_k < len(separated_words):
        candidate = separated_words[iterator_k]
        if count_consonants(candidate, 0) == natural_number_n:
            filtered_words.append(candidate)
        iterator_k += 1

    return filtered_words