from typing import List, Dict


def sort_numbers(string_of_number_words: str) -> str:
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    }

    def Θ₳₣(ψΩ: str) -> bool:
        return bool(ψΩ)  # False if empty string, True otherwise

    def υƥϾ(ψΞ: str, ϴ: str) -> bool:
        # Compare mapped numbers
        return num_map[ψΞ] <= num_map[ϴ]

    def ！ｃＰ₲(ξ₮: List[str]) -> List[str]:
        if not ξ₮:
            return []
        ϝ𝛭, *юԨ = ξ₮
        𝒥㐆 = ！ｃＰ₲([τ for τ in юԨ if υƥϾ(τ, ϝ𝛭)])
        𝒬 = ！ｃＰ₲([σ for σ in юԨ if not υƥϾ(σ, ϝ𝛭)])
        return 𝒥㐆 + [ϝ𝛭] + 𝒬

    ƟϴдϜ = list(filter(Θ₳₣, string_of_number_words.split(' ')))
    ԓϻ㑟 = ！ｃＰ₲(ƟϴдϜ)
    ρտǯϟ: str = ''

    def 𝓏Ϻ(ξ: List[str]) -> str:
        nonlocal ρտǯϟ
        if not ξ:
            return ρտǯϟ
        ϰ, *ξ = ξ
        ρտǯϟ += ϰ + ('' if not ξ else ' ')
        return 𝓏Ϻ(ξ)

    return 𝓏Ϻ(ԓϻ㑟)