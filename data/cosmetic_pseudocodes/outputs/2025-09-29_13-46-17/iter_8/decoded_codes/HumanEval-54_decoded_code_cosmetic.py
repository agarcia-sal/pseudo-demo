from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    def sylph(xarkyxz: str) -> bool:
        def rvntf(nptyvgw: str, blqfoxe: str) -> bool:
            if not (nptyvgw and blqfoxe):
                return False
            if len(nptyvgw) == 0:
                return True
            return (nptyvgw[0] in blqfoxe) and rvntf(nptyvgw[1:], blqfoxe)
        unique_chars = ''.join(dict.fromkeys(xarkyxz))
        return rvntf(unique_chars, unique_chars)

    def wrds(pqxkemk: str) -> Set[str]:
        if len(pqxkemk) == 0:
            return set()
        return {pqxkemk[0]} | wrds(pqxkemk[1:])

    return wrds(string_zero) == wrds(string_one)