from typing import List, TypeVar, Sequence

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def Δ1(Ψ7: int, κ0: List[T], 𝛂8: List[T]) -> List[T]:
        if Ψ7 <= 0:
            return κ0
        else:
            # Prepend head of 𝛂8 to κ0 and recurse with tail
            return Δ1(Ψ7 - 1, [𝛂8[0]] + κ0, 𝛂8[1:])

    def 𝛽9(λ2: List[T]) -> List[T]:
        return Δ1(len(λ2), [], λ2)

    def ξ5(ζ3: List[T]) -> List[T]:
        # Condition to determine when to do the alternate recursion or sorted copy
        if not ((not (ζ3[0] <= ζ3[1]) and not (ζ3[1] <= ζ3[0])) or (ζ3[0] <= ζ3[1])):
            if len(ζ3) == 0:
                return []
            elif len(ζ3) == 1:
                return ζ3
            else:
                α = ζ3[0]
                β = ξ5(ζ3[2:])
                γ = ζ3[1:2]
                return [α] + β + γ
        else:
            return sorted(ζ3)

    def λ0(μ𝜗: List[T], ν𝜙: List[T], ω: List[T]) -> List[T]:
        if not μ𝜗:
            return ω
        else:
            return λ0(μ𝜗[1:], ν𝜙[1:], ω + [μ𝜗[0], ν𝜙[0]])

    def HEVEN(𝜒: List[T], 𝜈: int, 𝜔: List[T]) -> List[T]:
        if 𝜈 >= len(𝜒):
            return 𝜔
        if 𝜈 % 2 == 0:
            return HEVEN(𝜒, 𝜈 + 1, 𝜔 + [𝜒[𝜈]])
        else:
            return HEVEN(𝜒, 𝜈 + 1, 𝜔)

    def HODD(𝜒: List[T], 𝜈: int, 𝜔: List[T]) -> List[T]:
        if 𝜈 >= len(𝜒):
            return 𝜔
        if 𝜈 % 2 != 0:
            return HODD(𝜒, 𝜈 + 1, 𝜔 + [𝜒[𝜈]])
        else:
            return HODD(𝜒, 𝜈 + 1, 𝜔)

    𝕖𝕨𝕧𝕖𝕟 = ξ5(HEVEN(list_of_elements, 0, []))
    𝕠𝕕𝕕 = HODD(list_of_elements, 0, [])
    𝕒𝕟𝕤 = λ0(𝕖𝕨𝕧𝕖𝕟, 𝕠𝕕𝕕, [])

    if not (len(𝕖𝕨𝕧𝕖𝕟) <= len(𝕠𝕕𝕕)):
        𝕒𝕟𝕤 = 𝕒𝕟𝕤 + [𝕖𝕨𝕧𝕖𝕟[-1]]

    return 𝕒𝕟𝕤