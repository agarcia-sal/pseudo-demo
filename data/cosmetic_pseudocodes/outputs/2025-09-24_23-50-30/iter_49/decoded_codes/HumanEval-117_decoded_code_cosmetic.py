from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_items: List[str] = []

    def count_non_vowels(rec_word: str, idx_count: int, consonant_count: int) -> int:
        if idx_count >= len(rec_word):
            return consonant_count
        current_char_lower = rec_word[idx_count].lower()
        is_consonant_flag = current_char_lower not in {'a', 'e', 'i', 'o', 'u'} and current_char_lower.isalpha()
        updated_consonant_count = consonant_count + (1 if is_consonant_flag else 0)
        return count_non_vowels(rec_word, idx_count + 1, updated_consonant_count)

    for word_item in string_s.split(" "):
        consonants_in_word = count_non_vowels(word_item, 0, 0)
        if consonants_in_word == natural_number_n:
            collected_items.append(word_item)

    return collected_items