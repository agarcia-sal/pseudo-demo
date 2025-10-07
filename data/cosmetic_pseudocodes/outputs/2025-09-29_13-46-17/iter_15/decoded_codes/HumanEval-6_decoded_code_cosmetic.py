from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(dσϙλ: str) -> int:
        def mλẎζ(Γ: int, ϝϾ: int) -> int:
            return Γ if Γ >= ϝϾ else ϝϾ

        def recursive_scan(τ҂: int, Ɣʭ: str, χα: int) -> int:
            if τ҂ == 0:
                return χα
            ϛႧ = τ҂ - 1
            Ƃƃ = χα
            if ξϢ(Ɣʭ[ϛႧ]) == '(':
                Ƃƃ = mλẎζ(Ɣʭ[ϛႧ] + 1, χα)
                return recursive_scan(ϛႧ, Ɣʭ, Ƃƃ)
            else:
                return recursive_scan(ϛႧ, Ɣʭ, χα)

        def ξϢ(Λ: str) -> str:
            return ')' if Λ == '(' else '('

        def count_maximum(ι: int, θ: int, ζ: int) -> int:
            if ι == len(dσϙλ):
                return θ
            λϗ = θ
            if dσϙλ[ι] == '(':
                return count_maximum(ι + 1, λϗ + 1, mλẎζ(λϗ + 1, ζ))
            else:
                return count_maximum(ι + 1, λϗ - 1, ζ)

        return count_maximum(0, 0, 0)

    def fold_groups(ωβɉ: int, ϮϠ: List[str], ζ: List[int]) -> List[int]:
        if ωβɉ == 0:
            return ζ
        κȏ = ωβɉ - 1
        ʎө = ζ
        σθ = ϮϠ[κȏ]
        if σθ != "":
            ʎө = [parse_paren_group(σθ)] + ζ
        return fold_groups(κȏ, ϮϠ, ʎө)

    κπיות: List[str] = []
    ϫϜν = 0
    Ωργ = len(parentheses_string)

    def split_acc(χζɛ: int) -> List[str]:
        nonlocal ϫϜν
        if χζɛ == Ωργ:
            return κπיות
        ϙւ = ""
        while ϫϜν < Ωργ and parentheses_string[ϫϜν] != " ":
            ϙւ += parentheses_string[ϫϜν]
            ϫϜν += 1
        if ϙւ != "":
            κπίες.append(ϙւ)
        ϫϜν = ϫϜν + 1
        return split_acc(ϫϜν)

    τϝ = split_acc(0)
    return fold_groups(len(τϝ), τϝ, [])