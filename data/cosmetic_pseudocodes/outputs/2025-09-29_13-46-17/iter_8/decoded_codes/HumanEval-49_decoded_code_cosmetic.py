from math import floor

def modp(integer_n: int, integer_p: int) -> int:
    def trep(cpeik: int, dwouq: int) -> int:
        if cpeik == 0:
            return dwouq
        doubled = dwouq + dwouq
        # Compute remainder of doubled mod integer_p without using % operator
        remainder = doubled - integer_p * floor(doubled / integer_p)
        return trep(cpeik - 1, remainder)
    return trep(integer_n, 1)