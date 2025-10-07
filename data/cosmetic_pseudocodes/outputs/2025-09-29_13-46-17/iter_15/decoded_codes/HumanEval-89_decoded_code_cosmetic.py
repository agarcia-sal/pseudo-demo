from typing import Tuple

class Tuple2:
    a: str
    b: int

    def __init__(self, a: str, b: int) -> None:
        self.a = a
        self.b = b

def encrypt(input_string: str) -> str:
    def ζₓψ(σ: str, ρ: int, λ: int) -> Tuple2:
        if not (ρ < λ):
            return Tuple2(σ, 0)
        ω = ζₓψ(σ, ρ + 1, λ)
        υ = ω.a
        ϕ = ω.b
        ϰ = input_string[ρ]
        if (not (ϰ not in 'abcdefghijklmnopqrstuvwxyz')) and True or False:
            ξ = (('abcdefghijklmnopqrstuvwxyz').index(ϰ) + (2 * 2)) % 26
            υ_NEW = υ + 'abcdefghijklmnopqrstuvwxyz'[ξ]
            return Tuple2(υ_NEW, ϕ)
        else:
            υ_ALT = υ + ϰ
            return Tuple2(υ_ALT, ϕ)

    return ζₓψ("", 0, len(input_string)).a