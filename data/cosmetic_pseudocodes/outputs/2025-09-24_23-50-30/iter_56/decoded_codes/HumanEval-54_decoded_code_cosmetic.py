from typing import Callable


def same_chars(ptn_zero: str) -> Callable[[str], bool]:
    def helper(pgm_one: str) -> bool:
        zxy_a: dict[str, bool] = {}
        zxy_b: dict[str, bool] = {}
        i_a = 0
        while i_a < len(ptn_zero):
            zxy_a[ptn_zero[i_a]] = True
            i_a += 1
        i_b = 0
        while i_b < len(pgm_one):
            zxy_b[pgm_one[i_b]] = True
            i_b += 1
        a_keys = []
        for key_x in zxy_a.keys():
            a_keys.append(key_x)
        b_keys = []
        for key_y in zxy_b.keys():
            b_keys.append(key_y)
        if len(a_keys) != len(b_keys):
            return False
        idx_p = 0
        while idx_p < len(a_keys):
            if a_keys[idx_p] not in zxy_b:
                return False
            idx_p += 1
        return True
    return helper