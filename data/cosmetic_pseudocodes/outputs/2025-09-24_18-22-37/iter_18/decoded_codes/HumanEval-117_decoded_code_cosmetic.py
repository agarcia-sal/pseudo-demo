from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_collection: List[str] = []
    word_sequence = string_s.split(' ')
    position = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while position < len(word_sequence):
        current_element = word_sequence[position]
        consonant_tally = 0
        character_counter = 0

        while True:
            if character_counter >= len(current_element):
                break
            current_letter_lower = current_element[character_counter].lower()
            if current_letter_lower not in vowels:
                consonant_tally += 1
            character_counter += 1

        if consonant_tally == natural_number_n:
            output_collection.append(current_element)

        position += 1

    return output_collection