from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_accumulator: List[str] = []

    def consonant_counter(word_x: str) -> int:
        def count_consonants(word_x: str, idx_j: int, acc_k: int) -> int:
            if idx_j >= len(word_x):
                return acc_k
            char_temp = word_x[idx_j].lower()
            is_vowel = char_temp in {'a', 'e', 'i', 'o', 'u'}
            new_acc = acc_k + (0 if is_vowel else 1)
            return count_consonants(word_x, idx_j + 1, new_acc)
        return count_consonants(word_x, 0, 0)

    def process_words(word_list_wl: List[str], idx_p: int) -> None:
        if idx_p == len(word_list_wl):
            return
        word_now = word_list_wl[idx_p]
        c_count = consonant_counter(word_now)
        if c_count == natural_number_n:
            result_accumulator.append(word_now)
        process_words(word_list_wl, idx_p + 1)

    word_collection = string_s.split(" ")
    process_words(word_collection, 0)
    return result_accumulator