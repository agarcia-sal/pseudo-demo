from typing import Callable

def encrypt(input_string: str) -> str:
    alphabet_sequence = "abcdefghijklmnopqrstuvwxyz"

    def helper_process_char(pos: int, result_accum: str) -> str:
        if pos == len(input_string):
            return result_accum
        current_elem = input_string[pos]

        def find_char_index(idx: int, found: int) -> int:
            if idx == len(alphabet_sequence):
                return found
            elif alphabet_sequence[idx] == current_elem:
                return find_char_index(idx + 1, idx)
            else:
                return find_char_index(idx + 1, found)

        real_index = find_char_index(0, -1)

        if real_index >= 0:
            computed_index = (real_index + 4) % 26
            updated_string = result_accum + alphabet_sequence[computed_index]
        else:
            updated_string = result_accum + current_elem

        return helper_process_char(pos + 1, updated_string)

    return helper_process_char(0, "")