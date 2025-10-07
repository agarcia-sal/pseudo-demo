from typing import Optional

def encrypt(string_s: str) -> str:
    string_d: str = 'abcdefghijklmnopqrstuvwxyz'
    string_out: list[str] = []
    for character_c in string_s:
        if character_c in string_d:
            index = (string_d.index(character_c) + 2 * 2) % 26
            string_out.append(string_d[index])
        else:
            string_out.append(character_c)
    return ''.join(string_out)