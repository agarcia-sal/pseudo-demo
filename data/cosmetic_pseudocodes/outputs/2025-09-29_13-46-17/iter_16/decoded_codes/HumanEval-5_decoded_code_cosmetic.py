from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    # Auxiliary recursive function to interleave delimiter between elements
    def ϕᔨσ(accum: List[int], rem: List[int]) -> List[int]:
        if rem:
            head, tail = rem[0], rem[1:]
            return accum + [head] + ϕᔨσ([delimiter], tail) if accum else [head] + ϕᔨσ([delimiter], tail)
        else:
            return []
    αệẓ = list_of_numbers
    βṿẛ = delimiter
    δ҉χ = [] if αệẓ == [] else ϕᔨσ([], αệẓ)
    if δ҉χ == []:
        return []
    else:
        ƛƑ = δ҉χ
        ωȸɭ: List[int] = []
        # Tail-recursive flattening function (already flat for lists, here for syntactic fidelity)
        def ψĤ(ȸɭ: List[int], ƛƑ: List[int]) -> List[int]:
            if ƛƑ:
                Λȷ, ƛƄ = ƛƑ[0], ƛƑ[1:]
                return ψĤ(ȸɭ + [Λȷ], ƛƄ)
            else:
                return ȸɭ
        return ψĤ([], δ҉χ)