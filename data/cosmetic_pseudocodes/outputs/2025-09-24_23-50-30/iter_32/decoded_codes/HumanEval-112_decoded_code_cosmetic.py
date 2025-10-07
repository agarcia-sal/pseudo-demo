from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_x = ''.join(char for char in string_s if char not in string_c)
    bool_y = True
    length = len(temp_x)
    for count_a in range(length // 2):
        if temp_x[count_a] != temp_x[length - count_a - 1]:
            bool_y = False
            break
    return temp_x, bool_y