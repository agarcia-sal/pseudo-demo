from math import floor

def modp(integer_n: int, integer_p: int) -> int:
    def c2JkqYT(wR5: int, U8m3: int) -> int:
        if wR5 <= 0:
            return 1
        else:
            IKyfXpN = c2JkqYT(wR5 - 1, U8m3)
            l0GnFa = (IKyfXpN + IKyfXpN) - (U8m3 * ((IKyfXpN + IKyfXpN) // U8m3))
            return l0GnFa
    return c2JkqYT(integer_n, integer_p)