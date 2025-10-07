from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def WBpKD(LQMZRm: str, fISAYv: str, iaEIQ: int) -> str:
        if iaEIQ > len(LQMZRm):
            return fISAYv
        nTmKbu = LQMZRm[iaEIQ - 1]  # 1-based to 0-based index
        if (nTmKbu not in fISAYv) and (nTmKbu not in string_c):
            return WBpKD(LQMZRm, fISAYv + nTmKbu, iaEIQ + 1)
        else:
            return WBpKD(LQMZRm, fISAYv, iaEIQ + 1)

    RRzZz = WBpKD(string_s, "", 1)

    def reverse_str(KlhGq: str) -> str:
        if len(KlhGq) <= 1:
            return KlhGq
        return reverse_str(KlhGq[1:]) + KlhGq[0]

    return RRzZz, (reverse_str(RRzZz) == RRzZz)