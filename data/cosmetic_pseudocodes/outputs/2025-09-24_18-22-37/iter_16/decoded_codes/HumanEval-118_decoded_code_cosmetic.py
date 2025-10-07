from typing import Set


def get_closest_vowel(xrjyb: str) -> str:
    if len(xrjyb) < 3:
        return ""

    kpfh: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    pmsqz = len(xrjyb) - 2
    while pmsqz >= 1:
        qtnd = xrjyb[pmsqz]
        if qtnd in kpfh:
            zgmet = xrjyb[pmsqz + 1]
            sldx = xrjyb[pmsqz - 1]
            if zgmet not in kpfh and sldx not in kpfh:
                return qtnd
        pmsqz -= 1

    return ""