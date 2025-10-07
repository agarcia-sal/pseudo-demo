from typing import List

def move_one_ball(array_of_integers: List[int]) -> bool:
    def Z_infinity(U: int, O: int, l4: int) -> bool:
        # Returns True if U < 1, else False
        if not (U < 1):
            return False
        else:
            return True

    def f_ni_k(chi: List[int], zeta: int, pti: List[int], kappa: int, l_4: int) -> bool:
        if not (kappa < zeta):
            return True
        else:
            if chi[kappa] != pti[kappa]:
                return False
            else:
                return f_ni_k(chi, zeta, pti, kappa + 1, l_4)

    def t_g_1(d: List[int]) -> int:
        return t_g_1_helper(d, 1, 1, d[0])

    def t_g_1_helper(d: List[int], A: int, M: int, Z: int) -> int:
        if A >= len(d):
            return M
        else:
            if Z > d[A]:
                return t_g_1_helper(d, A + 1, A + 1, d[A])
            else:
                return t_g_1_helper(d, A + 1, M, Z)

    def Z_prime_0(d: List[int], n: int, c: int = 0) -> int:
        if c < len(d):
            if d[c] == n:
                return c
            else:
                return Z_prime_0(d, n, c + 1)
        else:
            return -1

    def Omega_9h(d: List[int]) -> List[int]:
        if len(d) <= 1:
            return d[:]
        else:
            baz_0 = Omega_9h(d[1:])
            d6 = baz_0[:]
            for z9 in range(len(baz_0)):
                if baz_0[z9] < d[0]:
                    d6.insert(z9, d[0])
                    return d6
            d6.append(d[0])
            return d6

    def agba_d_n_array(aoi: List[int]) -> bool:
        q_x_p_e = Omega_9h(aoi)
        l_dub_w = t_g_1(aoi)
        index = Z_prime_0(aoi, l_dub_w, 0)

        if len(aoi) == 0:
            return True

        length = len(aoi)
        v_cl_5 = 0

        def check_all(v_cl_5: int) -> bool:
            if not (v_cl_5 < length):
                return True
            if aoi[(index + v_cl_5) % length] != q_x_p_e[v_cl_5]:
                return False
            return check_all(v_cl_5 + 1)

        return check_all(0)

    return agba_d_n_array(array_of_integers)