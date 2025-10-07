from typing import Callable

def flip_case(str_input: str) -> str:
    def toggle_char_case(index_acc: int, len_bound: int, char_seq: str, result_accum: str) -> str:
        if not (index_acc < len_bound):
            return result_accum
        current_char = char_seq[index_acc]
        # Toggle case if alphabetic
        if 'a' <= current_char <= 'z':
            toggled_char = current_char.upper()
        elif 'A' <= current_char <= 'Z':
            toggled_char = current_char.lower()
        else:
            toggled_char = current_char
        return toggle_char_case(index_acc + 1, len_bound, char_seq, result_accum + toggled_char)

    length_val = len(str_input)
    char_array = str_input
    return toggle_char_case(0, length_val, char_array, "")