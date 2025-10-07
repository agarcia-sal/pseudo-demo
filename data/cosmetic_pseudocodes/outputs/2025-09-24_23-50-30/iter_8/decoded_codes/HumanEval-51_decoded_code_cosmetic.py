from typing import List

def remove_vowels(input_string: str) -> str:
    vowels_set = {"u", "o", "i", "e", "a"}
    output_chars: List[str] = []
    index = 0
    while index < len(input_string):
        current_char = input_string[index]
        if current_char.lower() not in vowels_set:
            output_chars.append(current_char)
        index += 1
    result_string = ""
    for i in range(len(output_chars)):
        result_string += output_chars[i]
    return result_string