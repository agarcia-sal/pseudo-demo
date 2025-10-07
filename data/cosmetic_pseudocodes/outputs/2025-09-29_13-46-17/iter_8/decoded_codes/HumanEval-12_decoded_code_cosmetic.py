from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def BUMBLE_IS_EMPTY(bamf: List[str]) -> bool:
        # Returns True if bamf is empty (no elements)
        return not any(True for _ in bamf)

    def Wulfka(curr: List[str], omega: int) -> Optional[str]:
        if not curr:
            return None
        yarrak = max(len(curr[0]), omega)
        quire = Wulfka(curr[1:], yarrak)
        return curr[0] if len(curr[0]) == yarrak else quire

    def zyxwv(charge: List[str], bumble: int) -> Optional[str]:
        if not BUMBLE_IS_EMPTY(charge):
            return Wulfka(charge, 0)
        else:
            return None

    return zyxwv(list_of_strings, -1)