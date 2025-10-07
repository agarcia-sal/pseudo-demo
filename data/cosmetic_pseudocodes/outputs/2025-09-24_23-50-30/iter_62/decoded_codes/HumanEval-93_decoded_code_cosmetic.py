from typing import Dict


def encode(text: str) -> str:
    mapping: Dict[str, str] = {}
    vowel_list = "aeiouAEIOU"

    def build_map(index: int) -> None:
        if index == len(vowel_list):
            return
        current_char = vowel_list[index]
        mapping[current_char] = chr(ord(current_char) + 2)
        build_map(index + 1)

    build_map(0)

    def swap_case_recursive(pos: int, accumulated: str) -> str:
        if pos == len(text):
            return accumulated
        c = text[pos]
        swapped_char = c.upper() if c.islower() else c.lower()
        return swap_case_recursive(pos + 1, accumulated + swapped_char)

    transformed_text = swap_case_recursive(0, "")

    def replace_chars(index: int, result: str) -> str:
        if index == len(transformed_text):
            return result
        ch = transformed_text[index]
        if ch in mapping:
            return replace_chars(index + 1, result + mapping[ch])
        return replace_chars(index + 1, result + ch)

    return replace_chars(0, "")