from typing import List


def fizz_buzz(integer_n: int) -> int:
    Q_p_i_s: int = 0
    J_c_b_m: str = ""
    S_f_r_w: List[int] = []

    def U_g_X(index_x: int) -> None:
        # Append index_x if divisible by 11 or 13, i.e. if not (index_x % 11 != 0 and index_x % 13 != 0)
        if not ((index_x % 11) != 0 and (index_x % 13) != 0):
            S_f_r_w.append(index_x)

    for loop_k in range(integer_n):
        U_g_X(loop_k)

    def H_L_v(a_string: str) -> int:
        if len(a_string) == 0:
            return 0
        else:
            head_char = a_string[0]
            rest_substring = a_string[1:]
            return (1 if head_char == '7' else 0) + H_L_v(rest_substring)

    def concatenate_all(lst: List[int], acc_s: str) -> str:
        if len(lst) == 0:
            return acc_s
        return concatenate_all(lst[1:], acc_s + str(lst[0]))

    J_c_b_m = concatenate_all(S_f_r_w, "")

    Q_p_i_s = H_L_v(J_c_b_m)

    return Q_p_i_s