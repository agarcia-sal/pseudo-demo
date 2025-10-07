from typing import List


def same_chars(str_a: str, str_b: str) -> bool:
    unique_a: List[str] = []
    unique_b: List[str] = []
    for char_x in str_a:
        if char_x not in unique_a:
            unique_a.append(char_x)
    for i in range(len(str_b)):
        char_y = str_b[i]
        if char_y not in unique_b:
            unique_b.append(char_y)
    unique_a.sort()
    unique_b.sort()
    if len(unique_a) != len(unique_b):
        return False
    for j in range(len(unique_a)):
        if unique_a[j] != unique_b[j]:
            return False
    return True