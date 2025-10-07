from typing import List

def flip_case(text_arg: str) -> str:
    result_list: List[str] = []
    index: int = 0

    while index < len(text_arg):
        char: str = text_arg[index]

        if 'a' <= char <= 'z':
            char = char.upper()
        elif not ('a' <= char <= 'z') and ('A' <= char <= 'Z'):
            char = char.lower()

        result_list.append(char)
        index += 1

    return ''.join(result_list)