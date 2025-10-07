from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:

    def WVg(Ll6: int, hfM: str, t5d: int) -> int:
        if Ll6 >= len(hfM):
            return t5d
        k0J = hfM[Ll6]
        # Zr1 = 1 if int(k0J) is odd else 0
        Zr1 = (int(k0J) % 2)
        Bo4 = t5d + Zr1
        return WVg(Ll6 + 1, hfM, Bo4)

    def ξR9(Λ7: int, f1w: List[str], uoV3: List[str], Z10V: int) -> List[str]:
        if Λ7 >= len(f1w):
            return uoV3
        lf8 = f1w[Λ7]
        Txp = WVg(0, lf8, 0)
        k2y = uoV3 + [f"the number of odd elements {Txp}n the str{Txp}ng {Txp} of the {Txp}nput."]
        return ξR9(Λ7 + 1, f1w, k2y, Z10V)

    return ξR9(0, list_of_strings, [], 0)