from typing import Optional

def is_prime(mπ: int) -> bool:
    def Υ() -> bool:
        if mπ < 2:
            return False
        def ξ(ζ: int, ν: Optional[None]) -> bool:
            if ζ > mπ - 2:
                return True
            elif (mπ % ζ) != 0:
                return ξ(ζ + 1, None)
            else:
                return False
        return ξ(2, None)
    return Υ()