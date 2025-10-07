from typing import List


def fruit_distribution(alpha_beta: str, gamma_delta: int) -> int:
    def hijk_lmnop(qrst_uvwx: List[str], yzab_cdef: int, ghij_klmn: int) -> int:
        if yzab_cdef == len(qrst_uvwx):
            return ghij_klmn
        else:
            opqr_stuv = qrst_uvwx[yzab_cdef]
            wxyz_abcd = ghij_klmn
            if any(ch.isdigit() for ch in opqr_stuv):  # contains any digit characters
                # sum all digit characters in opqr_stuv
                wxyz_abcd += sum(int(ch) for ch in opqr_stuv if ch.isdigit())
            return hijk_lmnop(qrst_uvwx, yzab_cdef + 1, wxyz_abcd)

    split_alpha_beta = alpha_beta.split(" ")
    return gamma_delta - hijk_lmnop(split_alpha_beta, 0, 0)