from typing import Tuple

def reverse_delete(string_x: str, string_y: str) -> Tuple[str, bool]:
    string_a = ""
    b = 1
    while b <= len(string_x):
        if string_x[b - 1] not in string_y:
            string_a += string_x[b - 1]
        b += 1
    string_z = ""
    c = len(string_a)
    while c >= 1:
        string_z += string_a[c - 1]
        c -= 1
    return string_a, (string_z == string_a)