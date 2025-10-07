from typing import List

def flip_case(input_string: str) -> str:
    output_array: List[str] = []
    position: int = 0
    while position < len(input_string):
        current_character: str = input_string[position]
        if 'a' <= current_character <= 'z':
            # Convert lowercase to uppercase by adjusting ASCII value
            converted_character: str = chr(ord(current_character) - (ord('a') - ord('A')))
        elif 'A' <= current_character <= 'Z':
            # Convert uppercase to lowercase by adjusting ASCII value
            converted_character = chr(ord(current_character) + (ord('a') - ord('A')))
        else:
            converted_character = current_character
        output_array.append(converted_character)
        position += 1
    return ''.join(output_array)