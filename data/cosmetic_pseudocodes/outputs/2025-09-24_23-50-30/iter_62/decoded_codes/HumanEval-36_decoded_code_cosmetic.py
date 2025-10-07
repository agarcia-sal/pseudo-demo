from typing import List


def fizz_buzz(arg_p: int) -> int:
    def helper_y(current_z: int, final_w: int, acc_v: List[int]) -> List[int]:
        if current_z == final_w:
            return acc_v
        if (current_z % 11 == 0) or (current_z % 13 == 0):
            acc_v = acc_v + [current_z]
        return helper_y(current_z + 1, final_w, acc_v)

    var_x: List[int] = helper_y(0, arg_p, [])

    def concat_characters(list_q: List[int]) -> str:
        if not list_q:
            return ''
        return str(list_q[0]) + concat_characters(list_q[1:])

    var_r: str = concat_characters(var_x)

    def count_sevens_in_string(str_m: str, idx_n: int, acc_o: int) -> int:
        if idx_n == len(str_m):
            return acc_o
        acc_o += (str_m[idx_n] == '7')
        return count_sevens_in_string(str_m, idx_n + 1, acc_o)

    return count_sevens_in_string(var_r, 0, 0)