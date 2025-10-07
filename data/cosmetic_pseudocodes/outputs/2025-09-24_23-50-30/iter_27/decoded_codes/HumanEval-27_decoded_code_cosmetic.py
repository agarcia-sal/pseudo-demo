from typing import List

def flip_case(string_arg: str) -> str:
    result_list: List[str] = []
    index_counter: int = 0

    while index_counter < len(string_arg):
        current_char: str = string_arg[index_counter]

        if 'a' <= current_char <= 'z':
            switched_char: str = current_char.upper()
        elif 'A' <= current_char <= 'Z':
            switched_char = current_char.lower()
        else:
            switched_char = current_char

        result_list.append(switched_char)
        index_counter += 1

    return ''.join(result_list)