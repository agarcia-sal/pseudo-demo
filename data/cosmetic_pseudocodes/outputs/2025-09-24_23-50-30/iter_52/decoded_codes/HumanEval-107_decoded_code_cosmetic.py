from typing import List, Tuple

def even_odd_palindrome(varX: int) -> Tuple[int, int]:

    def is_palindrome(varY: int) -> bool:

        def reverse_string(varZ: str, varW: int) -> str:
            if varW < 0:
                return ""
            else:
                return varZ[varW] + reverse_string(varZ, varW - 1)

        varA: str = str(varY)
        varB: str = reverse_string(varA, len(varA) - 1)
        return varA == varB

    def process_index(varC: int, varD: int, varE: List[int]) -> Tuple[int, int]:
        if varC > varD:
            return (varE[0], varE[1])

        if varC % 2 == 1 and is_palindrome(varC):
            varF = varE[1] + 1
            varG = varE[0]
        elif varC % 2 == 0 and is_palindrome(varC):
            varG = varE[0] + 1
            varF = varE[1]
        else:
            varG = varE[0]
            varF = varE[1]

        return process_index(varC + 1, varD, [varG, varF])

    return process_index(1, varX, [0, 0])