from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    filtered_chars = []
    for index in range(len(s)):
        current_char = s[index]
        found_in_c = False
        for c_index in range(len(c)):
            if current_char == c[c_index]:
                found_in_c = True
                break
        if not found_in_c:
            filtered_chars.append(current_char)
    s = ''
    for i in range(len(filtered_chars)):
        s += filtered_chars[i]
    reversed_s = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    if reversed_s == s:
        return s, True
    else:
        return s, False