from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonant_chars(array_chars: List[str]) -> int:
        position = 0
        consonant_counter = 0
        while position < len(array_chars):
            ch = array_chars[position].lower()
            if ch in {'a', 'e', 'i', 'o', 'u'}:
                position += 1
                continue
            consonant_counter += 1
            position += 1
        return consonant_counter

    list_alpha = string_s.split(" ")
    filtered_collection: List[str] = []
    iterator_v = 0
    while iterator_v < len(list_alpha):
        word_instance = list_alpha[iterator_v]
        if count_consonant_chars([char for char in word_instance]) == natural_number_n:
            filtered_collection.append(word_instance)
        iterator_v += 1
    return filtered_collection