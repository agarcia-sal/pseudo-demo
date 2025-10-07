from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_list: list[str] = [char_x for char_x in string_s if char_x not in string_c]
    new_str: str = "".join(temp_list)

    def is_equal(str_a: str, str_b: str) -> bool:
        if len(str_a) != len(str_b):
            return False
        count_j = 0
        while count_j < len(str_a):
            if str_a[count_j] != str_b[count_j]:
                return False
            count_j += 1
        return True

    def reverse_string(str_p: str) -> str:
        result_str = ""
        position_k = len(str_p) - 1
        while position_k >= 0:
            result_str += str_p[position_k]
            position_k -= 1
        return result_str

    reversed_str = reverse_string(new_str)
    palindrome_flag = is_equal(new_str, reversed_str)
    return new_str, palindrome_flag