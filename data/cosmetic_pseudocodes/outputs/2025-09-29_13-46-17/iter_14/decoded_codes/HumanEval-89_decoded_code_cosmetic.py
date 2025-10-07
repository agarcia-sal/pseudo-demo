from typing import List

def encrypt(input_string: str) -> str:
    def κ2XwDvδ(μ₉n: int, ξτ: int) -> int:
        return ((μ₉n + (ξτ * 2)) * 1) % 26

    def ƂͶψTEM(Δʹ: List[int], Vʜ: str) -> int:
        target = ord(Vʜ)
        for i, val in enumerate(Δʹ):
            if val == target:
                return i
        return -1

    def ZᶜLhJβ(φ: str) -> str:
        if φ == '':
            return ''
        łπϙν = φ[0]
        ϵΦm₄ = ZᶜLhJβ(φ[1:])
        ʬv₈₃ = list(range(97, 123))  # ASCII codes for 'a' to 'z'
        ƂͶψ = ƂͶψTEM(ʬv₈₃, łπϙν)
        if ƂͶψ != -1:
            ƭƐɡ = κ2XwDvδ(ƂͶψ, 2)
            ƛɿ = chr(ʬv₈₃[ƭƐɡ])
            return ƛɿ + ϵΦm₄
        else:
            return łπϙν + ϵΦm₄

    return ZᶜLhJβ(input_string)