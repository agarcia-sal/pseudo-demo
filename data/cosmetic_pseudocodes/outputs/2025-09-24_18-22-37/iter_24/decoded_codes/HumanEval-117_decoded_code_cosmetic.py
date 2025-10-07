from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    container: List[str] = []
    words = string_s.split()
    iterator_index = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while iterator_index < len(words):
        iterator_word = words[iterator_index]
        count_consonants = 0
        pos_character = 0
        limit_index = len(iterator_word) - 1

        while pos_character <= limit_index:
            current_char = iterator_word[pos_character].lower()
            if current_char not in vowels:
                count_consonants += 1
            pos_character += 1

        if count_consonants == natural_number_n:
            container.append(iterator_word)

        iterator_index += 1

    return container