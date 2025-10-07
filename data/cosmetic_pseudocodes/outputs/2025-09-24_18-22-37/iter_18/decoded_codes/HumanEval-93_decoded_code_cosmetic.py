from typing import Dict


def encode(ciphertext: str) -> str:
    vowels_collection: str = "aeiouAEIOU"
    temp_map: Dict[str, str] = {}
    counter: int = 0
    while True:
        if counter > len(vowels_collection) - 1:
            break
        current_symbol = vowels_collection[counter]
        shifted_symbol = chr(ord(current_symbol) + 2)
        temp_map[current_symbol] = shifted_symbol
        counter += 1

    flipped_text: str = ""
    index_var: int = 0
    while index_var < len(ciphertext):
        original_char = ciphertext[index_var]
        if original_char in vowels_collection:
            flipped_text += temp_map[original_char]
        else:
            flipped_text += original_char
        index_var += 1

    output_string: str = ""
    position: int = 0
    while position < len(flipped_text):
        character_to_flip = flipped_text[position]
        if character_to_flip.islower():
            flipped_character = character_to_flip.upper()
        elif character_to_flip.isupper():
            flipped_character = character_to_flip.lower()
        else:
            flipped_character = character_to_flip
        output_string += flipped_character
        position += 1

    return output_string