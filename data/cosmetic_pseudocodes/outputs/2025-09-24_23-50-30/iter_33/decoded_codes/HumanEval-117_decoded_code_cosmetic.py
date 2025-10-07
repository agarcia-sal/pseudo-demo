from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    words_list: List[str] = string_s.split(" ")

    def check_consonant_count(curr_word: str, counter: int, position: int, limit: int) -> int:
        if position > limit:
            return counter
        char_lower = curr_word[position].lower()
        is_consonant = char_lower not in {"a", "e", "i", "o", "u"}
        return check_consonant_count(curr_word, counter + int(is_consonant), position + 1, limit)

    def process_words(index: int, boundary: int, collected: List[str]) -> List[str]:
        if index >= boundary:
            return collected
        word_candidate = words_list[index]
        consonants_found = check_consonant_count(word_candidate, 0, 0, len(word_candidate) - 1)
        filtered_list = collected + [word_candidate] if consonants_found == natural_number_n else collected
        return process_words(index + 1, boundary, filtered_list)

    return process_words(0, len(words_list), [])