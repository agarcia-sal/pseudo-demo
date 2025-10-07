from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def auxiliary_function(ξχζΩ: int, αβγδε: List[int]) -> bool:
        if not αβγδε:
            return False
        ψπ, *ωτφ = αβγδε
        ζμν = ξχζΩ + ψπ
        if ζμν < 0:
            return True
        return auxiliary_function(ζμν, ωτφ)
    return auxiliary_function(0, list_of_operations)