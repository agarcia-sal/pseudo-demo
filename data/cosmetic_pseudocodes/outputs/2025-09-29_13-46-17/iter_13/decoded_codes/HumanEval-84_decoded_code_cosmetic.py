from typing import Callable


def solve(integer_N: int) -> str:
    def helper_φΞ₁(str_ωζ: str, idx_σΨ: int, acc_яЮ: int) -> int:
        if idx_σΨ == len(str_ωζ):
            return acc_яЮ
        δҨǃ = acc_яЮ + ord(str_ωζ[idx_σΨ]) - ord('0')
        return helper_φΞ₁(str_ωζ, idx_σΨ + 1, δҨǃ)

    ξ҂Ѡ = str(integer_N)
    Σπ₄ = helper_φΞ₁(ξ҂Ѡ, 0, 0)

    def binrec_ΛΨ(μЯκ: int) -> str:
        if μЯκ == 0:
            return ""
        aҐ₉ = μЯκ % 2
        РхЧ = binrec_ΛΨ(μЯκ // 2)
        return РхЧ + str(aҐ₉)

    ӨڪӇ = binrec_ΛΨ(Σπ₄)
    ϾфҨ = ӨڪӇ[2:]
    return ϾфҨ