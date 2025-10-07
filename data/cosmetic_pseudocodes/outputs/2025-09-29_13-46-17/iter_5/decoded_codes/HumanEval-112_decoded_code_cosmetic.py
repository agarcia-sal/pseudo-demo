from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    acc_chars_cam_12 = ""
    idx_k_001 = 1
    length_s = len(string_s)
    while idx_k_001 <= length_s:
        char_Ux9 = string_s[idx_k_001 - 1]
        if char_Ux9 not in string_c:
            acc_chars_cam_12 += char_Ux9
        idx_k_001 += 1

    isSymBoolean = True
    left_M4 = 1
    right_Bz5 = len(acc_chars_cam_12)
    while left_M4 < right_Bz5:
        left_char = acc_chars_cam_12[left_M4 - 1]
        right_char = acc_chars_cam_12[right_Bz5 - 1]
        if left_char != right_char:
            isSymBoolean = False
            break
        left_M4 += 1
        right_Bz5 -= 1

    return acc_chars_cam_12, isSymBoolean