from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants_in_word(list_c: List[str], integer_i: int, integer_total: int) -> int:
        if integer_i >= len(list_c):
            return integer_total
        letter = list_c[integer_i].lower()
        is_vowel = letter in {"a", "e", "i", "o", "u"}
        return count_consonants_in_word(list_c, integer_i + 1, integer_total + (0 if is_vowel else 1))

    def process_words(list_w: List[str], list_acc: List[str]) -> List[str]:
        if not list_w:
            return list_acc
        current_word = list_w[0]
        cons_count = count_consonants_in_word(list(current_word), 0, 0)
        new_acc = list_acc + [current_word] if cons_count == natural_number_n else list_acc
        return process_words(list_w[1:], new_acc)

    return process_words(string_s.split(" "), [])