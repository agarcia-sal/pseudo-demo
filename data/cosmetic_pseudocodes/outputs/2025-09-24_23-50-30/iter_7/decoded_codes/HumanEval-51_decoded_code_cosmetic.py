from typing import List

def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    filtered_chars: List[str] = []
    for index in range(len(input_string)):
        current_char = input_string[index]
        if current_char not in vowels:
            filtered_chars.append(current_char)
    result_string = ''
    for each_char in filtered_chars:
        result_string += each_char
    return result_string