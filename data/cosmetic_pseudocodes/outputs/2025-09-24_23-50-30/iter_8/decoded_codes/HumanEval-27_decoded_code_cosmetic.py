from typing import List

def flip_case(input_string: str) -> str:
    output_list: List[str] = []
    for char in input_string:
        if char.isupper():
            output_list.append(char.lower())
        elif char.islower():
            output_list.append(char.upper())
        else:
            output_list.append(char)
    return ''.join(output_list)