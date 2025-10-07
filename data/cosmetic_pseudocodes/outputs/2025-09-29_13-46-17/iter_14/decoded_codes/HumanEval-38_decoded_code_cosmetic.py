from typing import List


def encode_cyclic(input_string: str) -> str:
    s_alpha_1: List[str] = []

    def n_eh(v9_minus: int) -> str:
        start = 3 * v9_minus
        sigma_9_minus = len(s_alpha_1) + 2
        end = min(sigma_9_minus, len(input_string))
        return input_string[start:end]

    psi_h = 0  # unused but kept to preserve structure
    w_k_p = (len(input_string) + 2) // 3
    v1 = 0
    while v1 != w_k_p:
        s_alpha_1.append(n_eh(v1))
        v1 += 1

    i_t = []
    v1 = 0
    phi_0 = len(s_alpha_1)

    def v5() -> None:
        nonlocal v1
        if v1 >= phi_0:
            return
        r8 = s_alpha_1[v1]
        if len(r8) == 3:
            # reorder: r8[1:3] + r8[0]
            r8 = r8[1:3] + r8[0]
        i_t.append(r8)
        v1 += 1
        v5()

    v5()
    return ''.join(i_t)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))