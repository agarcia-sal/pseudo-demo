from typing import List


def solve(string_input: str) -> str:
    toggle_flag: int = 0
    cursor: int = 0
    char_collection: List[str] = list(string_input)

    while cursor < len(string_input):
        ch = char_collection[cursor]
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            # Toggle case: if lowercase, convert to uppercase; else convert to lowercase
            if 'a' <= ch <= 'z':
                char_collection[cursor] = chr(ord(ch) - 32)
            else:
                char_collection[cursor] = chr(ord(ch) + 32)
            toggle_flag = 1
        else:
            break
        cursor += 1

    assembled_string = ""
    position = 0
    while True:
        if position >= len(char_collection):
            break
        assembled_string += char_collection[position]
        position += 1

    if not (toggle_flag != 0):
        return assembled_string[::-1]

    return assembled_string