from typing import List

def flip_case(alphanumeric_input: str) -> str:
    output_collection: List[str] = []
    position_counter: int = 0
    length: int = len(alphanumeric_input)
    while position_counter < length:
        current_character: str = alphanumeric_input[position_counter]
        if 'a' <= current_character <= 'z':
            transformed_character = chr(ord(current_character) - 32)
        elif 'A' <= current_character <= 'Z':
            transformed_character = chr(ord(current_character) + 32)
        else:
            transformed_character = current_character
        output_collection.append(transformed_character)
        position_counter += 1
    return ''.join(output_collection)