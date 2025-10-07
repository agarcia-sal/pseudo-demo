from typing import List


def flip_case(str_param: str) -> str:
    index_counter: int = 0
    transformed_chars: List[str] = []

    while index_counter < len(str_param):
        current_char: str = str_param[index_counter]

        if 'a' <= current_char <= 'z':
            transformed_chars.append(current_char.upper())
        elif 'A' <= current_char <= 'Z':
            transformed_chars.append(current_char.lower())
        else:
            transformed_chars.append(current_char)

        index_counter += 1

    return ''.join(transformed_chars)