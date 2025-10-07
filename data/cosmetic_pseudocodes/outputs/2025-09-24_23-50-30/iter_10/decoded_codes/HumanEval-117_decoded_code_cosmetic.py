from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_non_vowels(text_word: str) -> int:
        consonant_count = 0
        position = 0
        vowels = {"a", "e", "i", "o", "u"}
        while position < len(text_word):
            if text_word[position].lower() not in vowels:
                consonant_count += 1
            position += 1
        return consonant_count

    collection_result: List[str] = []
    word_list = string_s.split(" ")
    for item_word in word_list:
        if count_non_vowels(item_word) == natural_number_n:
            collection_result.append(item_word)
    return collection_result