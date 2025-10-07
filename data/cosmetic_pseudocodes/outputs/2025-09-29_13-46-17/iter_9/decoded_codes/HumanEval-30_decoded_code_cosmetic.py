from typing import List

def get_positive(ζσφ: List[int]) -> List[int]:
    Λµ_β = lambda Γκν, Ψπ: Γκν + [Ψπ] if Ψπ > 0 else Γκν
    result: List[int] = []
    for x in reversed(ζσφ):
        result = Λµ_β(result, x)
    return result