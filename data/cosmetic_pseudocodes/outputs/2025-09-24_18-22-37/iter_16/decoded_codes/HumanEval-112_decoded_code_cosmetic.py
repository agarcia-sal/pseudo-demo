from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = ""
    idx = 0
    # Filter out characters from string_s that appear in string_c[0:10] explicitly checked
    while idx < len(string_s):
        current_char = string_s[idx]
        if not (
            (len(string_c) > 0 and string_c[0] == current_char) or
            (len(string_c) > 1 and string_c[1] == current_char) or
            (len(string_c) > 2 and string_c[2] == current_char) or
            (len(string_c) > 3 and string_c[3] == current_char) or
            (len(string_c) > 4 and string_c[4] == current_char) or
            (len(string_c) > 5 and string_c[5] == current_char) or
            (len(string_c) > 6 and string_c[6] == current_char) or
            (len(string_c) > 7 and string_c[7] == current_char) or
            (len(string_c) > 8 and string_c[8] == current_char) or
            (len(string_c) > 9 and string_c[9] == current_char)
        ):
            filtered_chars += current_char
        idx += 1

    reversed_filtered_chars = ""
    backward_index = len(filtered_chars) - 1
    while backward_index >= 0:
        reversed_filtered_chars += filtered_chars[backward_index]
        backward_index -= 1

    if reversed_filtered_chars == filtered_chars:
        return filtered_chars, True
    else:
        return filtered_chars, False