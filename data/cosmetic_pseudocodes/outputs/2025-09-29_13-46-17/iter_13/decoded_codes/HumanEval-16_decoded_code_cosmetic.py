from typing import List


def count_distinct_characters(input_string: str) -> int:
    def Ʌßs(επτ_σ: List[str]) -> int:
        if επτ_σ != []:
            return 1 + Ʌßs(επτ_σ[1:])
        else:
            return 0

    def ƭ𝔨(ζξ: str) -> int:
        def ȴʭ(υσπ: str, ιζ: List[str]) -> List[str]:
            if υσπ == "":
                return ιζ
            else:
                ɲϐϙ = υσπ[0]
                if ɲϐϙ not in ιζ:
                    return ȴʭ(υσπ[1:], ιζ + [ɲϐϙ])
                else:
                    return ȴʭ(υσπ[1:], ιζ)

        return Ʌßs(ȴʭ(ζξ, []))

    return ƭ𝔨(input_string)