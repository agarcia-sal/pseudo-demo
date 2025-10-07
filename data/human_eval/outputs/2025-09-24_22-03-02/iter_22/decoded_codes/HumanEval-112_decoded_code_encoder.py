from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    filtered_characters = []
    for i in range(len(s)):
        char = s[i]
        found_in_c = False
        for j in range(len(c)):
            if char == c[j]:
                found_in_c = True
                break
        if not found_in_c:
            filtered_characters.append(char)
    s = ''
    for k in range(len(filtered_characters)):
        s += filtered_characters[k]
    reversed_s = ''
    for m in range(len(s) - 1, -1, -1):
        reversed_s += s[m]
    is_palindrome = reversed_s == s
    return s, is_palindrome