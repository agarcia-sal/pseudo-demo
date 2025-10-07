from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    b: list[str] = []
    x: int = 0

    while x < len(string_s):
        if string_s[x] in string_c:
            x += 1
            continue
        b.append(string_s[x])
        x += 1

    string_s = "".join(b)
    y: int = 0
    z: int = len(string_s) - 1
    result: bool = True

    while y < z:
        if string_s[y] != string_s[z]:
            result = False
            break
        y += 1
        z -= 1

    return string_s, result