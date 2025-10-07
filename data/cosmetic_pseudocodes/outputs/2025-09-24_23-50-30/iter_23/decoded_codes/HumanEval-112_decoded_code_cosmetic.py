from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    buffer_list = [element for element in string_s if element not in string_c]
    string_s = ''.join(buffer_list)
    return string_s, string_s == string_s[::-1]