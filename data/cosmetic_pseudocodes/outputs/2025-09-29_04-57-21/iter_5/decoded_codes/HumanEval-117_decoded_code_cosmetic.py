from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_collection: List[str] = []

    def count_consonants(text: str) -> int:
        count = 0
        position = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while position < len(text):
            current_letter = text[position].lower()
            if current_letter.isalpha() and current_letter not in vowels:
                count += 1
            position += 1
        return count

    words_list = string_s.split(" ")
    index = 0
    while index < len(words_list):
        word_item = words_list[index]
        if count_consonants(word_item) == natural_number_n:
            result_collection.append(word_item)
        index += 1

    return result_collection