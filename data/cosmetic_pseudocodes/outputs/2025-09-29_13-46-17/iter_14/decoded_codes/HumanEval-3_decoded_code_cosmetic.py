from typing import List, Callable

def below_zero(list_of_operations: List[int]) -> bool:
    def mU90ήλ(🜂: List[int], 𝓷: int) -> bool:
        if 𝓷 != 0:
            𝖵𝔦 = 🜂[0] + 𝓷
            if 𝖵𝔦 < 0:
                return True
            return mU90ήλ(🜂[1:], 𝖵𝔦)
        else:
            return False
    return mU90ήλ(list_of_operations, 0)