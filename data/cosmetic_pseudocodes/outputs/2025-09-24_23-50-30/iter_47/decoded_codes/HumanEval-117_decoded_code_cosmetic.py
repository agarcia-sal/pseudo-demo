from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    word_index: int = 0
    words_array: List[str] = string_s.split(" ")
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while word_index < len(words_array):
        current_word = words_array[word_index]
        consonant_count = 0
        char_index = 0

        while char_index < len(current_word):
            char_lower = current_word[char_index].lower()
            if char_lower not in vowels:
                consonant_count += 1
            char_index += 1

        if consonant_count == natural_number_n:
            output_list.append(current_word)

        word_index += 1

    return output_list