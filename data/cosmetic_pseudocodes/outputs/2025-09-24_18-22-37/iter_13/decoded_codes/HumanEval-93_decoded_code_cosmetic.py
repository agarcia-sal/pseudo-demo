from typing import Dict

def encode(input_text: str) -> str:
    swap_set: str = "AEIOUaeiou"
    translation_map: Dict[str, str] = {}

    index_counter: int = 0
    while index_counter < len(swap_set):
        current_char: str = swap_set[index_counter]
        ascii_val: int = ord(current_char)
        incremented_ascii: int = ascii_val + 2
        translated_char: str = chr(incremented_ascii)
        translation_map[current_char] = translated_char
        index_counter += 1

    swapped_text: str = ""
    walk_index: int = 0
    while walk_index < len(input_text):
        original_char: str = input_text[walk_index]
        if 'a' <= original_char <= 'z':
            # Convert lowercase to uppercase
            swapped_char: str = chr(ord(original_char) - (ord('a') - ord('A')))
        elif 'A' <= original_char <= 'Z':
            # Convert uppercase to lowercase
            swapped_char = chr(ord(original_char) + (ord('a') - ord('A')))
        else:
            swapped_char = original_char
        swapped_text += swapped_char
        walk_index += 1

    output_string: str = ""
    step_index: int = 0
    while True:
        if step_index >= len(swapped_text):
            break
        curr_char: str = swapped_text[step_index]
        if curr_char in translation_map:
            output_string += translation_map[curr_char]
        else:
            output_string += curr_char
        step_index += 1

    return output_string