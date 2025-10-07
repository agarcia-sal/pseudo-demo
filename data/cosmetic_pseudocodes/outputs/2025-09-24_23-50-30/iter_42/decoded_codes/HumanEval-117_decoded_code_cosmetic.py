from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(string_x: str, idx: int, acc: int) -> int:
        if idx >= len(string_x):
            return acc
        current_char_lower = string_x[idx].lower()
        is_vowel = current_char_lower in {'a', 'e', 'i', 'o', 'u'}
        next_acc = acc + (0 if is_vowel else 1)
        return count_consonants(string_x, idx + 1, next_acc)

    def process_words(lst: List[str], pos: int, res_acc: List[str]) -> List[str]:
        if pos >= len(lst):
            return res_acc
        current_word = lst[pos]
        consonant_count = count_consonants(current_word, 0, 0)
        new_res = res_acc + [current_word] if consonant_count == natural_number_n else res_acc
        return process_words(lst, pos + 1, new_res)

    word_list = string_s.split(" ")
    result_sequence: List[str] = []
    return process_words(word_list, 0, result_sequence)