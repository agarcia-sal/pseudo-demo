from typing import Set

def count_distinct_characters(varA: str) -> int:
    varB: str = varA.lower()
    varC: Set[str] = set()

    def iterate_chars(varD: str, varE: int) -> Set[str]:
        if varE == len(varD):
            return varC
        varC.add(varD[varE])
        return iterate_chars(varD, varE + 1)

    return len(iterate_chars(varB, 0))