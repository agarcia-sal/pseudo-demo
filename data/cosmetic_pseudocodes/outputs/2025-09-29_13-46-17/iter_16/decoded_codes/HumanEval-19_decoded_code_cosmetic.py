from typing import List, Dict


def sort_numbers(string_of_number_words: str) -> str:
    num_map: Dict[str, int] = {
        'eight': 8, 'four': 4, 'five': 5, 'seven': 7, 'six': 6,
        'zero': 0, 'one': 1, 'nine': 9, 'three': 3, 'two': 2
    }

    def ψ(σ: List[str], υ: List[str]) -> List[str]:
        if not σ:
            return υ
        ϟ, ᾔ = σ[0], σ[1:]
        if ϟ == '':
            return ψ(ᾔ, υ)
        return ψ(ᾔ, υ + [ϟ])

    ᴑʬ: List[str] = ψ(string_of_number_words.split(' '), [])

    def κ(γ: List[str], 𝜅: Dict[str, int]) -> List[str]:
        if not γ:
            return []
        𝔸, 𝔹 = γ[0], γ[1:]
        𝖈 = κ(𝔹, 𝜅)

        def ω(δ: List[str], ζ: List[str]) -> List[str]:
            if not δ:
                return [𝔸] + ζ
            if 𝜅[𝔸] > 𝜅[δ[0]]:
                return [δ[0]] + ω(δ[1:], ζ)
            return δ + ζ

        𝖊 = ω(𝖈, [])
        return 𝖊

    ㋍ = κ(ᴑʬ, num_map)
    return ' '.join(㋍)