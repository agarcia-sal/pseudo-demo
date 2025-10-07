from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    accumulator: List[str] = []
    words_collection: List[str] = string_s.split(" ")
    vowels = {"a", "e", "i", "o", "u"}

    def count_consonants_recursive(array_chars: List[str], curr_pos: int, end_pos: int, tally: int) -> int:
        if curr_pos > end_pos:
            return tally
        letter_lower = array_chars[curr_pos].lower()
        # Increment tally by 1 if letter is a consonant
        tally_updated = tally + (letter_lower not in vowels)
        return count_consonants_recursive(array_chars, curr_pos + 1, end_pos, tally_updated)

    def process_words_recursive(idx: int, max_idx: int) -> None:
        if idx > max_idx:
            return
        current_word = words_collection[idx]
        consonant_num = count_consonants_recursive(list(current_word), 0, len(current_word) - 1, 0)
        if consonant_num == natural_number_n:
            accumulator.append(current_word)
        process_words_recursive(idx + 1, max_idx)

    process_words_recursive(0, len(words_collection) - 1)
    return accumulator