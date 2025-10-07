from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants_in_word(w: str, position: int, limit: int, count: int) -> int:
        if position >= limit:
            return count
        current_char = w[position].lower()
        is_consonant = current_char not in {"a", "e", "i", "o", "u"}
        return count_consonants_in_word(w, position + 1, limit, count + (1 if is_consonant else 0))

    accumulated_result: List[str] = []

    def process_words(word_list: List[str], idx: int, upper_bound: int) -> List[str]:
        if idx >= upper_bound:
            return accumulated_result
        current_word = word_list[idx]
        num_consonants = count_consonants_in_word(current_word, 0, len(current_word), 0)
        if num_consonants == natural_number_n:
            accumulated_result.append(current_word)
        return process_words(word_list, idx + 1, upper_bound)

    words_array = string_s.split(" ")
    return process_words(words_array, 0, len(words_array))