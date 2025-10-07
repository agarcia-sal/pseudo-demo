from typing import List

def encrypt(input_string: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    output_chars: List[str] = []

    def process_chars(pos: int) -> None:
        if pos == len(input_string):
            return
        current_char: str = input_string[pos]
        char_pos: int = -1
        i: int = 0

        def find_index() -> None:
            nonlocal i, char_pos
            if i == len(alphabet):
                return
            if alphabet[i] == current_char:
                char_pos = i
                return
            i += 1
            find_index()

        find_index()

        if char_pos >= 0:
            shift_val: int = ((char_pos + 2) * 2) % 26
            output_chars.append(alphabet[shift_val])
        else:
            output_chars.append(current_char)

        process_chars(pos + 1)

    process_chars(0)
    return "".join(output_chars)