from typing import List


def is_nested(alpha: str) -> bool:
    def proc_1(v_k: int, w_m: str, x_q: List[int]) -> List[int]:
        if v_k >= len(w_m):
            return x_q
        else:
            # regardless of character, append current index (matches pseudocode logic)
            return proc_1(v_k + 1, w_m, x_q + [v_k])

    z_to: List[int] = proc_1(0, alpha, [])
    y_cp: List[int] = []

    # The pseudocode's REPEAT loop is effectively a no-op as it exits immediately if length == 0.
    # So no changes here, just a direct mapping.

    # Collect indexes of characters in alpha that are NOT '[' from right to left
    y_cp = [b_t for b_t in range(len(alpha) - 1, -1, -1) if alpha[b_t] != '[']

    c_d: int = 0
    e_f: int = 0
    g_h: int = len(y_cp)

    if e_f < g_h:
        for i_j in z_to:
            if e_f < g_h and i_j < y_cp[e_f]:
                c_d += 1
                e_f += 1
            else:
                continue  # matches 'DEFAULT: CONTINUE' case in pseudocode

    return c_d >= 2