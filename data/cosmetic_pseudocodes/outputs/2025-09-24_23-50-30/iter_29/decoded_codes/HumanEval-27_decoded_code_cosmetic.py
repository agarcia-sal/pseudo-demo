from typing import List


def flip_case(str_param: str) -> str:
    idx_counter: int = 0
    result_builder: List[str] = []
    while idx_counter < len(str_param):
        current_char: str = str_param[idx_counter]
        if 'a' <= current_char <= 'z':
            result_builder.append(current_char.upper())
        elif 'A' <= current_char <= 'Z':
            result_builder.append(current_char.lower())
        else:
            result_builder.append(current_char)
        idx_counter += 1
    return ''.join(result_builder)