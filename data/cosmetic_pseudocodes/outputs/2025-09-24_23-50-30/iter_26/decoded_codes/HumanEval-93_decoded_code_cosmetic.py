from typing import Dict


def encode(input_string: str) -> str:
    def swap_case_map(char: str) -> str:
        if 'a' <= char <= 'z':
            return chr(ord(char) - 32)
        if 'A' <= char <= 'Z':
            return chr(ord(char) + 32)
        return char

    key_collection: str = "aeiouAEIOU"
    substitute_pairs: Dict[str, str] = {elem: chr(ord(elem) + 2) for elem in key_collection}

    def transform_case(s: str, index: int) -> str:
        if index >= len(s):
            return ""
        return swap_case_map(s[index]) + transform_case(s, index + 1)

    swapped_string: str = transform_case(input_string, 0)

    def build_result(s: str, curr_index: int) -> str:
        if curr_index == len(s):
            return ""
        current_char = s[curr_index]
        replaced_char = substitute_pairs.get(current_char, current_char)
        return replaced_char + build_result(s, curr_index + 1)

    return build_result(swapped_string, 0)