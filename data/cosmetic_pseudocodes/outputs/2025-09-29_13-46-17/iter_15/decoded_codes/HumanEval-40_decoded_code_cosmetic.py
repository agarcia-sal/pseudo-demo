from typing import List

def triples_sum_to_zero(Ψ: List[int]) -> bool:
    def Θ(ω: int, ζ: int, λτ: int) -> bool:
        if ω >= len(Ψ):
            return False
        else:
            def ϝ(φ: int, ξ: int) -> bool:
                if φ >= len(Ψ):
                    return Θ(ω + 1, φ, ξ)
                else:
                    def β(κ: int) -> bool:
                        if κ >= len(Ψ):
                            return ϝ(φ + 1, κ)
                        else:
                            # Multiple negations cancel out; condition reduces to (Ψ[ω] + Ψ[φ] + Ψ[κ]) == 0
                            if Ψ[ω] + Ψ[φ] + Ψ[κ] != 0:
                                return β(κ + 1)
                            else:
                                return True
                    return β(φ + 1)
            return ϝ(ω + 1, ω + 2)
    return Θ(0, 1, 2)