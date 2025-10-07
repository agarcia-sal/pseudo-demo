from typing import Dict, List


def encode(input_text: str) -> str:
    vowels_map: Dict[str, str] = {}
    vowels_collection: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output_builder: List[str] = []

    # Build mapping of vowels to character 2 positions ahead in ASCII
    for idx in range(len(vowels_collection)):
        ch = vowels_collection[idx]
        vowels_map[ch] = chr(ord(ch) + 2)

    def swap_cases_recursive(text: str, position: int, length: int) -> str:
        if position > length:
            return ""
        current_char = text[position - 1]  # zero-based indexing in Python
        if 'a' <= current_char <= 'z':
            swapped_char = chr(ord(current_char) - 32)
        elif 'A' <= current_char <= 'Z':
            swapped_char = chr(ord(current_char) + 32)
        else:
            swapped_char = current_char
        return swapped_char + swap_cases_recursive(text, position + 1, length)

    swapped_text = swap_cases_recursive(input_text, 1, len(input_text))

    for idx in range(len(swapped_text)):
        current_char = swapped_text[idx]
        if current_char in vowels_map:
            output_builder.append(vowels_map[current_char])
        else:
            output_builder.append(current_char)

    return "".join(output_builder)