from typing import Dict

def encode(sTrInG: str) -> str:
    vOwElS: str = "AEIOUaeiou"

    def build_map(idx: int, accum: Dict[str, str]) -> Dict[str, str]:
        if idx >= len(vOwElS):
            return accum
        k = vOwElS[idx]
        v = chr(ord(k) + 2)
        accum[k] = v
        return build_map(idx + 1, accum)

    transform_map: Dict[str, str] = build_map(0, {})

    def toggle_case(input_str: str, pos: int, result_acc: str) -> str:
        if pos == len(input_str):
            return result_acc
        curr_char = input_str[pos]
        if 'a' <= curr_char <= 'z':
            toggled_char = chr(ord(curr_char) - 32)
        elif 'A' <= curr_char <= 'Z':
            toggled_char = chr(ord(curr_char) + 32)
        else:
            toggled_char = curr_char
        return toggle_case(input_str, pos + 1, result_acc + toggled_char)

    toggled_message: str = toggle_case(sTrInG, 0, "")

    def replace_chars(str_in: str, curr_pos: int, acc_str: str) -> str:
        if curr_pos == len(str_in):
            return acc_str
        this_char = str_in[curr_pos]
        if this_char in transform_map:
            return replace_chars(str_in, curr_pos + 1, acc_str + transform_map[this_char])
        else:
            return replace_chars(str_in, curr_pos + 1, acc_str + this_char)

    return replace_chars(toggled_message, 0, "")