from typing import List

def remove_vowels(input_string: str) -> str:
    filtered_chars: List[str] = []
    index_counter: int = 0
    while index_counter < len(input_string):
        current_char: str = input_string[index_counter]
        lower_char: str = current_char.lower()
        exclusion_flag: bool = False
        if lower_char in ("a", "e", "i", "o", "u"):
            exclusion_flag = True
        else:
            exclusion_flag = False
        if not exclusion_flag:
            filtered_chars.append(current_char)
        index_counter += 1
    result_string: str = ""
    for element in filtered_chars:
        result_string += element
    return result_string