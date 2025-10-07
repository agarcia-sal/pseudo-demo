from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    gathered_words: List[str] = []
    word_position = 0
    word_array = string_s.split(" ")

    while word_position < len(word_array):
        current_word = word_array[word_position]
        cons_count = 0
        letter_pos = 0

        while letter_pos < len(current_word):
            letter = current_word[letter_pos]
            letter_lower = letter.lower()

            if letter_lower not in vowels:
                cons_count += 1

            letter_pos += 1

        if cons_count != natural_number_n:
            word_position += 1
            continue

        gathered_words.append(current_word)
        word_position += 1

    return gathered_words