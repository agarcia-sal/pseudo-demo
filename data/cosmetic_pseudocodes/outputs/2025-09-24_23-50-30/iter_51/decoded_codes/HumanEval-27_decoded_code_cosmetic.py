from typing import List

def flip_case(str_param: str) -> str:
    def flip_char(c_char: str) -> str:
        if 'a' <= c_char <= 'z':
            return chr(ord(c_char) - (ord('a') - ord('A')))
        elif 'A' <= c_char <= 'Z':
            return chr(ord(c_char) + (ord('a') - ord('A')))
        else:
            return c_char

    def recurse_flip(idx: int, acc_list: List[str]) -> str:
        if idx == len(str_param):
            return "".join(acc_list)
        else:
            return recurse_flip(idx + 1, acc_list + [flip_char(str_param[idx])])

    return recurse_flip(0, [])