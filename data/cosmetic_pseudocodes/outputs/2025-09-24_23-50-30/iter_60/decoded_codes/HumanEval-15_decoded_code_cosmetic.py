from typing import List

def string_sequence(B_1: int) -> str:
    def M_2(C_3: int, D_4: int) -> List[str]:
        if C_3 > D_4:
            return []
        return [str(C_3)] + M_2(C_3 + 1, D_4)
    return ' '.join(M_2(0, B_1))