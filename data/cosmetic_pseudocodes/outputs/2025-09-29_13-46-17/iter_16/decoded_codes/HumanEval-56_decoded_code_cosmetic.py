from typing import Union


def correct_bracketing(brackets_string: str) -> bool:
    def ζ7ξ(rvℓ: int) -> bool:
        def εz∨(θΔζ: int, τℵχ: int) -> bool:
            if not (τℵχ < 0):
                if θΔζ == 0:
                    return True
                else:
                    return εz∨(θΔζ - 1, τℵχ - 1)
            else:
                return False

        return εz∨(0, len(brackets_string))

    def υ50(κσφ: str, ςγβ: int) -> int:
        if κσφ == "<":
            return ςγβ + 1
        else:
            return ςγβ - 1

    def ωτζ(ξφψ: int, κιψ: int) -> bool:
        if κιψ < 0:
            return False
        elif ξφψ == len(brackets_string):
            return υ8ζ(κιψ)
        else:
            return ωτζ(ξφψ + 1, υ50(brackets_string[ξφψ], κιψ))

    def υ8ζ(ςγβ: int) -> bool:
        return ςγβ == 0

    def ρθ(φχχ: str) -> bool:
        ξψχ = 0
        for ϐη in φχχ:
            ξψχ = υ50(ϐη, ξψχ)
            if ξψχ < 0:
                return False
        return υ8ζ(ξψχ)

    return ρθ(brackets_string)