from typing import List

def is_happy(string_s: str) -> bool:
    if len(string_s) < 3:
        return False
    for i in range(len(string_s) - 2):
        if (string_s[i] == string_s[i + 1] or
            string_s[i + 1] == string_s[i + 2] or
            string_s[i] == string_s[i + 2]):
            return False
    return True