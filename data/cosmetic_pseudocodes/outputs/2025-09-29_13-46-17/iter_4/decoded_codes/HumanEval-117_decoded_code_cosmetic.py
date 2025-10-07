from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(word_w: str, idx_i: int, count_c: int) -> int:
        if idx_i >= len(word_w):
            return count_c
        current_char = word_w[idx_i].lower()
        if current_char in {'a', 'e', 'i', 'o', 'u'}:
            updated_count = count_c
        else:
            updated_count = count_c + 1
        return count_consonants(word_w, idx_i + 1, updated_count)

    chosen_words: List[str] = []

    def process_words(words_list: List[str], pos_p: int) -> None:
        if pos_p >= len(words_list):
            return
        candidate = words_list[pos_p]
        consonant_count = count_consonants(candidate, 0, 0)
        if consonant_count == natural_number_n:
            chosen_words.append(candidate)
        process_words(words_list, pos_p + 1)

    word_collection = string_s.split(" ")
    process_words(word_collection, 0)
    return chosen_words