from typing import List

def flip_case(alt_string: str) -> str:
    result_array: List[str] = []
    idx: int = 0
    while idx < len(alt_string):
        current_character: str = alt_string[idx]
        if current_character.islower():
            result_array.append(current_character.upper())
        elif current_character.isupper():
            result_array.append(current_character.lower())
        else:
            result_array.append(current_character)
        idx += 1
    return "".join(result_array)