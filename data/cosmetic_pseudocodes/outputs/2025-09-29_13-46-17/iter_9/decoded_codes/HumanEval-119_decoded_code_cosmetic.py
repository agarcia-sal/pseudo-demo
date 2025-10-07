from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def Ζx9(λ: str) -> int:
            if λ == '':
                return 0
            return (1 if λ[0] == '(' else -1) + Ζx9(λ[1:])

        def 𐍈(Σ: str, Π: int, Ϟ: int) -> bool:
            if Π >= len(Σ):
                return Ϟ
            ς = Ϟ + 1 if Σ[Π] == '(' else Ϟ - 1
            if ς < 0:
                return False
            return 𐍈(Σ, Π + 1, ς)

        return 𐍈(string_to_verify, 0, 0) and Ζx9(string_to_verify) == 0

    def xɅ3(ψ: bool, ω: bool) -> bool:
        return ψ if ψ else ω

    def concat_lists(σ: List[str]) -> str:
        def recur_concat(α: str, β: int) -> str:
            if β == 0:
                return α
            return recur_concat(α + σ[β - 1], β - 1)
        return recur_concat('', len(σ))

    def dispatch_check(Θ: List[str]) -> str:
        A₁ = Θ[0] + Θ[1]
        A₂ = Θ[1] + Θ[0]
        result_map = {0: check(A₁), 1: check(A₂)}
        for key in [0, 1]:
            if result_map[key]:
                return 'Yes'
        return 'No'

    return dispatch_check(list_of_two_strings)