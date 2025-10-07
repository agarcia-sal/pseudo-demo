from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_non_vowels(word_internal: str, idx_internal: int, accum_internal: int) -> int:
        if idx_internal > len(word_internal) - 1:
            return accum_internal
        if word_internal[idx_internal].lower() in {"a", "e", "i", "o", "u"}:
            return count_non_vowels(word_internal, idx_internal + 1, accum_internal)
        return count_non_vowels(word_internal, idx_internal + 1, accum_internal + 1)

    filtered_words: List[str] = []
    word_list = string_s.split(" ")

    def process_words(words_local: List[str], pos_local: int) -> None:
        if pos_local >= len(words_local):
            return
        measured = count_non_vowels(words_local[pos_local], 0, 0)
        if measured == natural_number_n:
            filtered_words.append(words_local[pos_local])
        process_words(words_local, pos_local + 1)

    process_words(word_list, 0)
    return filtered_words