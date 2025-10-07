from typing import Dict


def encode(message: str) -> str:
    vowels_reference: str = "aeiouAEIOU"
    mapping_table: Dict[str, str] = {}
    index: int = 0
    while index < len(vowels_reference):
        current_char: str = vowels_reference[index]
        shifted_char: str = chr(ord(current_char) + 2)
        mapping_table[current_char] = shifted_char
        index += 1

    def swapCase(text: str) -> str:
        position: int = 0
        result_chars = []
        while position < len(text):
            char = text[position]
            if char.islower():
                result_chars.append(char.upper())
            elif char.isupper():
                result_chars.append(char.lower())
            else:
                result_chars.append(char)
            position += 1
        return "".join(result_chars)

    altered_message: str = swapCase(message)

    output_chars = []
    pointer: int = 0
    while pointer < len(altered_message):
        current_char = altered_message[pointer]
        output_chars.append(mapping_table.get(current_char, current_char))
        pointer += 1

    return "".join(output_chars)