from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_sequence: List[str] = []
    word_queue: List[str] = string_s.split(" ")
    position: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while position < len(word_queue):
        current_word = word_queue[position]
        consonant_count = 0
        letter_index = 0
        while letter_index < len(current_word):
            letter = current_word[letter_index].lower()
            if letter in vowels:
                letter_index += 1
                continue
            else:
                consonant_count += 1
                letter_index += 1
        if consonant_count == natural_number_n:
            output_sequence.append(current_word)
        position += 1
    return output_sequence